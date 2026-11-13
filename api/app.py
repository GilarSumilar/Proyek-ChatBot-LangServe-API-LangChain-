from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server using LangChain Runnable Interfaces",
)

# Gemini Model
gemini_model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

# Ollama Model
ollama_model = ChatOllama(model="llama3.2:latest")

prompt_gemini = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt_ollama = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt_gemini | gemini_model,
    path="/gemini",
)

add_routes(
    app,
    prompt_ollama | ollama_model,
    path="/ollama",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

