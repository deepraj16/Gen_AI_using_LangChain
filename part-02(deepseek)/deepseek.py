from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"


llm = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)
response = llm.invoke("What is the capital of India?")
print(response.content)

