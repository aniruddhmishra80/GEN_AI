from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document Loader/GRU.pdf")
docs = data.load()

print(docs[0].page_content)
print(len(docs))