from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
from pathlib import Path

# data = PyPDFLoader("document_loaders/GRU.pdf")

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "GRU.pdf"   # if GRU.pdf is in the same folder as test.py

data = PyPDFLoader(str(file_path))

docs = data.load()

splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=10)
chunks = splitter.split_documents(docs)

for chunk in chunks:
    # print(chunk.metadata)
    print(chunk.page_content)
    print()
print(len(chunks))
