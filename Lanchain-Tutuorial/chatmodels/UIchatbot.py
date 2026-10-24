import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

MODES = {
    1: "you are a funny assistant",
    2: "you are a angry assistant",
    3: "you are a sad assistant",
}

st.set_page_config(page_title="Chatbot", page_icon="*")


@st.cache_resource
def get_model():
    return ChatMistralAI(
        model_name="codestral-latest",
        temperature=0.7,
    )


model = get_model()

st.title("Chatbot")

# choose the mode once, before the chat starts
if "messages" not in st.session_state:
    st.write("Enter Your response")
    mode = st.radio(
        "Mode",
        options=[1, 2, 3],
        format_func=lambda m: f"{m} - {MODES[m]}",
        label_visibility="collapsed",
    )
    if st.button("Start"):
        # short term memory
        st.session_state.messages = [SystemMessage(content=MODES[mode])]
        st.rerun()
    st.stop()

st.caption(st.session_state.messages[0].content)

# show the conversation so far
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

prompt = st.chat_input("user :")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    result = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=result.content))
    with st.chat_message("assistant"):
        st.write(result.content)

if st.button("End chat"):
    del st.session_state.messages
    st.rerun()