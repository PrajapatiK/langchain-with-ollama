from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

splitter = CharacterTextSplitter(separator="", chunk_size=10, chunk_overlap=1)

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "notes.txt"
data = TextLoader(str(file_path))
docs = data.load()

chunks = splitter.split_documents(docs)

# print(chunks)
for chunk in chunks:
    # print(chunk.metadata)
    print(chunk.page_content)
    print()
print(len(chunks))
