import requests
import streamlit as st

def get_gemini_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/gemini/invoke",
            json={"input": {"topic": input_text}},
        )
        data = response.json()
        output = data.get("output", {})
        if isinstance(output, dict):
            content = output.get("content", "")
            if isinstance(content, list):
                # Handle list of blocks (like text/thinking blocks in Gemini 3.5/3.8)
                return "".join([c.get("text", "") for c in content if isinstance(c, dict) and c.get("text")])
            return str(content) if content else str(output)
        return str(output)
    except Exception as e:
        return f"Error connecting to Gemini API route: {e}"

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/ollama/invoke",
            json={"input": {"topic": input_text}},
        )
        data = response.json()
        output = data.get("output", {})
        if isinstance(output, dict):
            content = output.get("content", "")
            if isinstance(content, list):
                return "".join([c.get("text", "") for c in content if isinstance(c, dict) and c.get("text")])
            return str(content) if content else str(output)
        return str(output)
    except Exception as e:
        return f"Error connecting to Ollama API route: {e}"

st.title("LangChain Client with LangServe")

input_text = st.text_input("Tulis topik untuk essay (Gemini):")
input_text1 = st.text_input("Tulis topik untuk puisi (Ollama - Llama 3.2):")

if input_text:
    with st.spinner("Memproses dengan Gemini..."):
        res = get_gemini_response(input_text)
        st.write(res)

if input_text1:
    with st.spinner("Memproses dengan Ollama..."):
        res1 = get_ollama_response(input_text1)
        st.write(res1)
