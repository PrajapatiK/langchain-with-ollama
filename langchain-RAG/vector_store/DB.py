from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "Python"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "Pandas"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "Neural Networks"}),
]

# embedding_model = OpenAIEmbeddings()
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(
    documents=docs, 
    embedding=embedding_model,
    persist_directory="test-chroma-db"
)

result = vector_store.similarity_search("What is used for data analysis?", k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriever = vector_store.as_retriever()

docs = retriever.invoke("Explain deep learning?")

for doc in docs:
    print(doc.page_content)