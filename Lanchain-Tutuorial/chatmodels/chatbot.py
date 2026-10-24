from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


load_dotenv()

model = ChatMistralAI(
    model_name = "codestral-latest",
    tempreture = 0.7
)
mode = int(input("Enter Your response"))
if(mode == 1):
    mode = "you are a funny assistant"
elif (mode == 2):
    mode = "you are a angry assistant"
elif (mode == 3):
    mode = "you are a sad assistant"
    
messages = [
    SystemMessage(content=mode)
    # set behaviour of the model 
] 
# short term memory
print("======================welcome to the chatbot")
while True:
    prompt = input("user :")
    if prompt == "0":
        break
    messages.append(HumanMessage(content=prompt))
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("bot :", result.content)

print(messages)
