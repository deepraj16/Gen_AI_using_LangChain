from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
import os
import streamlit as st  

load_dotenv()

st.header("Resarech tool") 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)


user_input=st.text_input("Enter your prompt")

if st.button("Sumarizer"):
    result=model.invoke(user_input) 
    st.text(result.content)
