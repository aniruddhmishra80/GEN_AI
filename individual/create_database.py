# load pdf
# split into chunks
# create the embeddings 
# strore into chroma 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv


# context window of mistralAI is 32k tokens
# PromptTemplate

load_dotenv()
data = PyPDFLoader("Document Loader/OReilly.Fundamentals.of.Deep.Learning.2017.5.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size  = 1000,
    chunk_overlap = 200
)
chunks = splitter.split_documents(docs)
# context window of mistralAI is 32k tokens
# PromptTemplate

embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)



