from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# data = PyPDFLoader("document_loaders/GRU.pdf")

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "GRU.pdf"   # if GRU.pdf is in the same folder as test.py

data = PyPDFLoader(str(file_path))

docs = data.load()

print(docs)
print(len(docs))
