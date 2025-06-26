from langchain_community.document_loaders import TextLoader 
from  langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
import os  
from dotenv import load_dotenv 

load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")
os.environ['OPENAI_API_KEY'] = api_key
print(api_key)
model=ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free", 
    max_tokens=900, 
    temperature=0.8,
     openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"
)

# print(model.invoke("what is a captail of india"))

prompt=PromptTemplate(template="""
            write a summary for the following inforamtion - \n {info}                      
""" , 
input_variables=['info'])


Docs=TextLoader(
    'working.txt', 
    encoding='utf-8'
)

loader=Docs.load()

parser = StrOutputParser()

chain = prompt | model | parser 

responce=chain.invoke({'info':loader[0].page_content})
print(responce)