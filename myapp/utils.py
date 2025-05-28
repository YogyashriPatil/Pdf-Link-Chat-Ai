import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCIEEu-SokOLeMDBFMfipcyvywCDoliUiY"

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

def pdf_Chat(name):
    pdf_path = Path(__file__).parent / name
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()
    print(docs[0])

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    split_docs = text_splitter.split_documents(documents=docs)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vector_store = QdrantVectorStore.from_documents(
        collection_name="wtl_project_pdf",
        url="http://localhost:6333",
        embedding=embeddings,
        documents=[]
    )
    vector_store.add_documents(documents=split_docs)
    print("Injection done")

pdf_Chat("harmony.pdf")
