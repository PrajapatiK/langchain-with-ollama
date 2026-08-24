from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(
    persist_directory="chroma-db", 
    embedding_function=embedding_model
)

retriever = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lamda_mult": 0.5
    },
)

llm = ChatMistralAI(model='mistral-small-latest')

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.
               Use ONLY the provided context to answer the question.
               If the answer is not present in the context,
               say: "I could not find the answer in the document."
            """
        ),
        (
            "human",
            """Context:
            {context}
            Question:
            {question}
            """
        )
    ]
)

print("\n===== RAG Search Results =====\n")
print("\n===== Press 0 to exit =====\n")

while True:
    query = input("You: ")
    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}\n")
