# load pdf
# split into chunks
# create the embeddings
# store into chroma vector db

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

base_dir = Path(__file__).resolve().parent
# file_path = base_dir / "document_loaders" / "notes.txt"
file_path = base_dir / "document_loaders" / "deeplearning.pdf"
data = PyPDFLoader(str(file_path))
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
    )
chunks = splitter.split_documents(docs)

# embedding_model = OpenAIEmbeddings()
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=chunks, 
    embedding=embedding_model,
    persist_directory="chroma-db"
)
