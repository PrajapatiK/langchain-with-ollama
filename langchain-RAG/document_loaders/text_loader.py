# from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import TextLoader

# load_dotenv()

# data = TextLoader("document_loaders/notes.txt")

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "notes.txt"   # if notes.txt is in the same folder as test.py

data = TextLoader(str(file_path))

docs = data.load()

print(docs[0].metadata)
print(docs[0].page_content)
