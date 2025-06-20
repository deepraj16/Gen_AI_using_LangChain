from langchain_anthropic import ChatAnthropic 
from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv 
from langchain.schema.runnable import RunnableParallel
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

model1 = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)

model2=ChatAnthropic()

prompt1=PromptTemplate(
    template="Generate short and simple notes following text {text}", 
    input_variables=['text']

)
prompt2=PromptTemplate(
    template="Generate  5 short question answer from the following text \n{text}", 
    input_variables=['text']
)
prompt3=PromptTemplate(
    template="Merage the both notes and quiz into a single document /n notes-->{notes} and quiz --> {quiz}", 
    input_variables=['notes','text']
)
parser=StrOutputParser()

paraller_chain=RunnableParallel(
    {'notes':prompt1 | model1 | parser,
     'quize':prompt2| model2| parser
    }
)

merge_chain = prompt3 | model1 | parser

chain = paraller_chain | merge_chain

text="""

"""

chain.invoke()

chain.get_graph().draw_ascii()
