from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    st.error("GOOGLE_API_KEY belum diatur. Tambahkan ke file .env atau environment variables.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = google_api_key
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Respond in the user's language and keep each response to at most 100 words.",
        ),
        ("user", "Question: {question}"),
    ]
)

st.title("LangChain Demo With Gemini API")

with st.form("chat_form"):
    input_text = st.text_input("Search the topic you want")
    submitted = st.form_submit_button("Submit")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=google_api_key,
    max_output_tokens=180,
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if submitted and input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
