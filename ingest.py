# import dependencies
import os
import sys

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Api_kry
def main() -> None:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GOOGLE_API_KEY environment variable. Set it before running ingest.py.")
        sys.exit(1)
# Pdf loader
    loader = PyPDFLoader("data/documents.pdf")
    docs = loader.load()
    print("Loaded PDF pages:", len(docs))
# chunking
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print("Created document chunks:", len(chunks))
# Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    vector_store = FAISS.from_documents(chunks, embeddings)

    os.makedirs("faiss_store", exist_ok=True)
    vector_store.save_local("faiss_store")
    print("Saved FAISS vector store in faiss_store/")


if __name__ == "__main__":
    main()
