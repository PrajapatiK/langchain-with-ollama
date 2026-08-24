# from langchain_community.retrievers import ArxivRetriever
import arxiv

client = arxiv.Client()


#create the retriever
# retriever = ArxivRetriever(
#     load_max_docs=2,
#     load_all_metadata=True,
# )

search = arxiv.Search(
    query="Large language models",
    max_results=3,
)

#query arixv
# docs = retriever.invoke("Large language models?")
results = client.results(search)


#print results
# for i, doc in enumerate(docs):
#     print(f"\nResult {i+1}:")
#     print(f"Title: {doc.metadata.get('Title')}")
#     print(f"Authors: {doc.metadata.get('Authors')}")
#     print(f"Summary: {doc.page_content[:500]}")  # Print first 500 characters of the summary
#     print()

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join(author.name for author in result.authors)}")
    print(f"Summary: {result.summary[:500]}")
    print(f"URL: {result.entry_id}")