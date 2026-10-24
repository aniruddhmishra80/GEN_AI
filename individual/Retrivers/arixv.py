from langchain_community.retrievers import ArxivRetriever

retriver = ArxivRetriever(
    load_max_docs= 2 ,
    load_all_available_meta=True
)

doc = retriver.invoke("large language models")

for i, docs in enumerate(doc):
    print(f"\nResult {i+1}")
    print("Title:", docs.metadata.get("Title"))
    print("Authors:", docs.metadata.get("Authors"))
    print("Summary:", docs.page_content)