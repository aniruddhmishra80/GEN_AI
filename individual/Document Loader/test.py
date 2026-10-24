from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter

# token based text spliiting considering each word as a token based on chunks size
# splitter = CharacterTextSplitter(
#     separator = "",
#     chunk_size = 10,
#     chunk_overlap = 1
# )
splitter = RecursiveCharacterTextSplitter( 
    chunk_size = 100,
    chunk_overlap = 10
)

data = PyPDFLoader("Document Loader/GRU.pdf")
docs = data.load()

chunks = splitter.split_documents(docs)


# for i in chunks:
#     print(i.page_content)
#     print()
#     print()
#     print()
#     print()
# print(docs[0].page_content)

# page content and meta data we only need page_content
# after converting sentences to embeddings u find similarity and set athreshold of 0.5 
# like if the similary is 0.4 then two individual vectore if it reaches threshold then same vectors
# RecursiveCharacterTextSplitter find /n/n and /n " " and do spltting on the basis of semantic meaning

print(len(chunks))