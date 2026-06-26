# import modules
import os
from dotenv import load_dotenv
load_dotenv()
print("API:",os.getenv("GOOGLE_API_KEY"))

import sys

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# load Faiss_store
def load_vector_store() -> FAISS:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GOOGLE_API_KEY environment variable. Set it before running app.py.")
        sys.exit(1)

# Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    return FAISS.load_local("faiss_store", embeddings, allow_dangerous_deserialization=True)


def build_prompt(context: str, query: str) -> str:
    return (
        "You are a helpful assistant. Use only the information from the provided context "
        "to answer the question. If the context does not contain the answer, say 'I don't know.'\n\n"
        "CONTEXT:\n"
        f"{context}\n\n"
        "QUESTION:\n"
        f"{query}\n\n"
        "ANSWER:"
    )


def main() -> None:
    if not os.path.isdir("faiss_store"):
        print("FAISS store not found. Run ingest.py first to build the vector index.")
        sys.exit(1)
#Gemeni model
    vector_store = load_vector_store()
    llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)

    print("Retrieval chatbot ready. Enter a question or type 'exit' to quit.")

    while True:
        query = input("\nYour question: ").strip()
        if query.lower() in {"exit", "quit", "q"}:
            print("Goodbye.")
            break
        if not query:
            continue

        docs = vector_store.similarity_search(query, k=3)
        if not docs:
            print("No matching documents found.")
            continue

        context = "\n\n".join(f"Document {i + 1}:\n{doc.page_content}" for i, doc in enumerate(docs))
        prompt = build_prompt(context, query)

        response = llm.generate([prompt])
        answer = response.generations[0][0].text.strip()

        print("\nAnswer:\n", answer)
        print("\nSources:")
        for i, doc in enumerate(docs, start=1):
            print(f" - chunk {i}: {doc.metadata}")


if __name__ == "__main__":
    main()
