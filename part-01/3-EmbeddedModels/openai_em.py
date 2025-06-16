from langchain_openai import OpenAIEmbeddings 
from dotenv import load_dotenv 

load_dotenv()

llm=OpenAIEmbeddings(model="text-embedding-3-larg",dimensions=32)

result=llm.embed_query("Delhi is captail of india")
print(result)