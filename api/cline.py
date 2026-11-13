import requests
import streamlit as st

def get_gemini_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"input": {"topic": input_text}},
        )
        data = response.json()
        output = data.get("output", {})
        if isinstance(output, dict):
            return output.get("content", str(output))
        return str(output)
    except Exception as e:
        return f"Error connecting to Gemini API route: {e}"

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"input": {"topic": input_text}},
        )
        data = response.json()
        output = data.get("output", {})
        if isinstance(output, dict):
            return output.get("content", str(output))
        return str(output)
    except Exception as e:
        return f"Error connecting to Ollama API route: {e}"

st.title("LangChain Client with LangServe")

input_text = st.text_input("Tulis topik untuk essay (Gemini):")
input_text1 = st.text_input("Tulis topik untuk puisi (Ollama - Llama 3.2):")

if input_text:
    st.write(get_gemini_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

