from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import streamlit as st


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Respond in the user's language and keep each response to at most 100 words.",
        ),
        ("user", "Question: {question}"),
    ]
)

st.title("Chatbot dengan Ollama (Llama 3.2)")

with st.form("chat_form"):
    input_text = st.text_input("Tulis pertanyaan Anda")
    submitted = st.form_submit_button("Kirim")

llm = ChatOllama(model="llama3.2:latest")
chain = prompt | llm | StrOutputParser()

if submitted and input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
