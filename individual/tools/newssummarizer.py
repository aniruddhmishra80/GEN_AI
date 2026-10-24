from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    max_new_tokens=512,
)
model = ChatHuggingFace(llm=llm)

search_tool = TavilySearchResults(max_results = 5)
prompt = ChatPromptTemplate.from_template("""
You are a summarization assistant
{news}
""")

chain = prompt | model | StrOutputParser()

news_result = search_tool.invoke("Latest AI model of 2026")

result = chain.invoke({"news" : news_result})

print(result)
