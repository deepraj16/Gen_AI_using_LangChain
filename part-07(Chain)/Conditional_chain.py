from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field 
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda #runable
import os
from dotenv import load_dotenv 
from langchain.schema.runnable import RunnableLambda
 
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
model1 = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    temperature=0.7,
    max_tokens=512,
)

class FeedBack(BaseModel): 
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment in positive or negative")

parser2=PydanticOutputParser(pydantic_object=FeedBack)    

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n  pass the input formate {fromate}", 
    input_variables=['feedback'],
    partial_variables={'fromate': parser2.get_format_instructions() }
)

classifer_chain = prompt1 | model1 | parser2 

# result=classifer_chain.invoke({'feedback': "This is a wonderful smartphone"}).sentiment 

# print(result)

# branch_chain  = RunnableBranch(  
#       (condition1,chain1),
#     (condition2 , chain2)
# )

prompt2=PromptTemplate(
    template="Write an approprate response to this positive feedback \n {feedback}", 
    input_variables=['feedback'], 

)

prompt3=PromptTemplate(
    template="Write an approprate response to this negative feedback \n {feedback}", 
    input_variables=['feedback'], 
    
)

branch_chain  = RunnableBranch(  
      (lambda x:x['sentiment'] == 'positive',prompt2 |model1 | parser),
    (lambda x:x['sentiment'] == 'negative' , prompt3 | model1 | parser), 
    RunnableLambda(lambda x: "could not find sentement")
)

chain = classifer_chain | branch_chain 

chain.invoke({'feedback':"this is terrable phone"}) 

print(chain.invoke({'feedback':"this is good phone"}))