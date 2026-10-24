from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_groq import ChatGroq
# model = ChatGroq(model = "meta-llama/llama-prompt-guard-2-22m")

# from langchain_mistralai import ChatMistralAI
# model = ChatMistralAI(model = "mistral-small-2603")

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash" , tempreture=0
)

response = model.invoke("give me a poem on what is machine learning!")
# mistral-small-2603
print(response.content)