from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser,JsonOutputKeyToolsParser 
from dotenv import load_dotenv 
import os 

load_dotenv() 

#model llm 

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)

prompt1=PromptTemplate(
    template="Genrerate a details on topic {input_var}", 
    input_variables=['input_var']
)

prompt2=PromptTemplate(
    template="Genrate a 5 pointer summary from following text \n {text}",
    input_variables=["text"]
)

parser=StrOutputParser()


chain = prompt1 | model | parser | prompt2 | model | parser  
print(chain)

