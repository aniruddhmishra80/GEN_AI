from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel , RunnablePassthrough , RunnableLambda

model = ChatMistralAI(
    model = "mistral-small-2603"
)

pareser = StrOutputParser()

explain_prompt = ChatPromptTemplate.from_messages(
    [("System" , "You are a code generator") ,
    ("Human" , "{topic}")
    ]
)

seq = model | explain_prompt | pareser
seq2 = RunnableParallel(
    {"code" : RunnablePassthrough() , 
     "explanation" : explain_prompt | model | pareser
    }
)

chain = seq | seq2

result = chain.invoke({"topic" : "please write a code for palindorme in python"})

print(result['code'])
print(result['explanation'])