import streamlit as st
import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI


model = ChatMistralAI(
    model = 
)

response = model.invoke("what is ur name")
print(response.page_content)
load_dotenv()