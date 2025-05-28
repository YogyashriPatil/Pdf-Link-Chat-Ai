from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings


pdf_path=Path(__file__).parent/"os.pdf"

loader=PyPDFLoader(file_path=pdf_path)

docs=loader.load()
# print(docs[0])
#pip install langchain_text_splitter
text_splitter= RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
split_docs=text_splitter.split_documents(documents=docs)
api_key="AIzaSyDRy36UNei42DJEJdwaBzj9lOh3-5rFGUM"
# pip install langchain_google_genai
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
# embeddings.embed_query("What's our Q1 revenue?")
# make docker-compose file
# docker compose -f docker-compose.yml up