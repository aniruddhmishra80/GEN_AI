from langchain.chat_models import init_chat_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from dotenv  import load_dotenv
load_dotenv()

embeddings  = GoogleGenerativeAIEmbeddings(
    model = 'gemini-embedding-001',
)
#embedding dimension measns length of each vector technically we store this embeddings in vector store
vector = embeddings.embed_query("my name is aniruddh")
print(vector)