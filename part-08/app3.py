from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv("OPENROUTER_API_KEY")
print("API Key loaded:", api_key)

os.environ['OPENAI_API_KEY'] = api_key
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",
    temperature=0.7,
    max_tokens=1000,
     openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"
)

# print(model.invoke("What is the capital of India?"))
# OPENROUTER_API_KEY=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  

prompt = PromptTemplate(
    template="give the notes on following topics \n {topic}",
    input_variables=['topic']
)

output = StrOutputParser()
chain = prompt | model | output

response = chain.invoke({'topic': 'india'})

print(response)
