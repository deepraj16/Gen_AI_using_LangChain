from langchain_huggingface import HuggingFacePipeline ,ChatHuggingFace ,HuggingFaceEndpoint
from langchain_core.chat_models import ChatModel
from dotenv import load_dotenv 
load_dotenv() 

llm = HuggingFaceEndpoint( 
    repo_id="meta-llama/Llama-2-7b-chat-hf", 
    task="text-generation",
    model_kwargs={"temperature": 0.1, "max_new_tokens": 512},
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of France?")
print(result)