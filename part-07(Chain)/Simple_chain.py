from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser,JsonOutputKeyToolsParser
import os 

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)

prompt= PromptTemplate(
    template="Generate 5 interesting facts about {topic}", 
    input_variables=['topic'] 
)

parser=StrOutputParser()

chain= prompt | model | parser 

result=chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph().draw_ascii()