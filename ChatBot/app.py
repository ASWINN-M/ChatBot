from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama 
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API")
prompt = ChatPromptTemplate.from_messages(
    [
        ('system' , "Reply to User queries"),
        ('user' , 'Question{question}')
    ]
)

st.title("ChatBot")
input_text = st.text_input("Something")

llm = Ollama(model = "llama3.2")
output_parse = StrOutputParser()
chain = prompt|llm|output_parse

if input_text:
    st.write(chain.invoke({'question': {input_text}}))
