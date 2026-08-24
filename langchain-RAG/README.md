# LangChain RAG Project

This project is a small LangChain-based Retrieval-Augmented Generation (RAG) learning workspace. It demonstrates how to:

- load documents from PDF, text, and web sources
- split text into chunks
- generate embeddings
- store vectors in Chroma
- retrieve relevant chunks
- answer questions using an LLM
- build a basic Streamlit RAG app

The project is organized as a set of practical examples and experiments for understanding the RAG pipeline.

---

## Project Structure

```text
langchain-RAG/
├── app_RAG.py
├── create_database.py
├── main.py
├── requirements.txt
├── chroma_db/
│   ├── chroma.sqlite3
│   └── <persisted-collection-folder>/
├── chroma-db/
│   ├── chroma.sqlite3
│   └── <persisted-collection-folder>/
├── document_loaders/
│   ├── GRU.pdf
│   ├── deeplearning.pdf
│   ├── notes.txt
│   ├── pdf_loader.py
│   ├── pdf_loader_with_recursive_char_text_splitter.py
│   ├── pdf_loader_with_token_splitter.py
│   ├── text_loader.py
│   ├── text_loader_with_char_text_splitter.py
│   └── webpage_loader.py
├── retrievers/
│   ├── arxiv_by_source_retriever.py
│   ├── mmr_search_strategy.py
│   └── multiquery_search_strategy.py
└── vector_store/
    └── DB.py
```

---

## Root Files

### app_RAG.py
This is the main Streamlit application.

It does the following:

- uploads a PDF in the browser
- loads the PDF with `PyPDFLoader`
- splits it into chunks using `RecursiveCharacterTextSplitter`
- creates embeddings with `HuggingFaceEmbeddings`
- stores the vectors in the local Chroma database under `chroma_db`
- loads the existing database when available
- uses `ChatMistralAI` to answer questions grounded in the retrieved document context

Run it with:

```bash
streamlit run app_RAG.py
```

### create_database.py
This script creates a vector database from a PDF file.

It:

- loads `document_loaders/deeplearning.pdf`
- splits the document into chunks
- generates embeddings
- saves the resulting vector store to `chroma-db`

This is a good example of a simple indexing pipeline for a local knowledge base.

### main.py
This script is a command-line RAG chat example.

It:

- loads a persisted Chroma database
- creates a retriever with MMR search
- builds a question-answer prompt
- accepts questions from the terminal
- asks an LLM for grounded answers using retrieved context

Run it with:

```bash
python main.py
```

### requirements.txt
This file contains the Python dependencies used across the project.

It includes:

- LangChain packages
- Chroma
- embedding libraries (`sentence-transformers`, `langchain-huggingface`)
- document loader dependencies (`pypdf`, `unstructured`, `beautifulsoup4`, `lxml`)
- environment variable support (`python-dotenv`)
- optional app packages like `streamlit`, `fastapi`, and `uvicorn`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Directory Breakdown

### document_loaders/
This folder contains examples of loading raw content and preparing it for indexing.

#### Files

- `pdf_loader.py`
  - loads a PDF file using `PyPDFLoader`
  - prints a list of document pages

- `pdf_loader_with_recursive_char_text_splitter.py`
  - loads a PDF
  - splits it using `RecursiveCharacterTextSplitter`
  - prints the resulting chunks

- `pdf_loader_with_token_splitter.py`
  - loads a PDF
  - splits it using `TokenTextSplitter`
  - shows token-based chunking

- `text_loader.py`
  - loads plain text files using `TextLoader`
  - prints metadata and content

- `text_loader_with_char_text_splitter.py`
  - loads `notes.txt`
  - uses `CharacterTextSplitter` to create smaller chunks

- `webpage_loader.py`
  - loads content from a web page using `WebBaseLoader`
  - prints metadata and page text

#### Sample data

- `notes.txt` — plain text example data
- `deeplearning.pdf` — a PDF used in the database creation example
- `GRU.pdf` — another PDF used in loader experiments

This folder is useful for understanding the first stage of a RAG system: document ingestion.

### retrievers/
This folder demonstrates different retrieval strategies used after the vector store is built.

#### Files

- `arxiv_by_source_retriever.py`
  - uses the ArXiv API to fetch research papers
  - demonstrates source-based retrieval from academic content

- `mmr_search_strategy.py`
  - creates a Chroma vector store from example documents
  - uses Maximal Marginal Relevance (MMR) as a retrieval strategy to balance relevance and diversity

- `multiquery_search_strategy.py`
  - shows how to create multiple reformulations of a user query and retrieve relevant documents via `MultiQueryRetriever`

These files are good examples of advanced retrieval behavior beyond simple similarity search.

### vector_store/
This folder contains a simple Chroma database example.

#### `DB.py`
This script:

- creates a small in-memory example document set
- generates embeddings
- creates a vector store with Chroma
- performs similarity and MMR retrieval
- prints the search results

It helps explain the core vector-search workflow used by a RAG app.

### chroma_db/ and chroma-db/
These are local Chroma persistence directories.

They store the generated vector database files, including:

- `chroma.sqlite3`
- embedded collection content saved by Chroma

These directories are created when you run the indexing scripts. They are the persistence layer that lets the app query previously indexed documents without reprocessing them every time.

---

## Typical RAG Workflow in This Project

The project follows this sequence:

1. Load content from a source (PDF, text, or web page)
2. Split the content into manageable chunks
3. Convert chunks to vectors using embeddings
4. Save vectors in Chroma
5. Query the vector store for relevant documents
6. Feed the retrieved context to a language model
7. Generate a grounded response

---

## Setup and Usage

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

The scripts call `load_dotenv()`, so a `.env` file in the project root is expected if needed.

For LLM access, you may need values such as:

```env
MISTRAL_API_KEY=your_key_here
```

Some scripts also include commented-out OpenAI references, so this project is flexible between different model providers.

### 4. Build the database

```bash
python create_database.py
```

### 5. Run the CLI chat app

```bash
python main.py
```

### 6. Run the Streamlit app

```bash
streamlit run app_RAG.py
```

---

## Notes

- This project is designed as a learning and experimentation workspace rather than a production-ready app.
- It intentionally mixes small examples, sample datasets, and persistence folders.
- The vector DB directories may be regenerated or replaced depending on the dataset you index.
- Some scripts are notebook-like experiments; others are focused examples for a single RAG concept.

---

## Summary

This directory covers the complete life cycle of a LangChain RAG pipeline:

- ingestion
- chunking
- embedding
- storage
- retrieval
- prompting
- LLM-based answer generation
- UI integration

If you are studying RAG step by step, this folder is a practical collection of examples showing each stage in a compact, beginner-friendly way.
