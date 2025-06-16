from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Make sure your .env file contains OPENROUTER_API_KEY

# Set OpenRouter configuration
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("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")  # your API key from openrouter.ai

# Use DeepSeek model via OpenRouter
llm = ChatOpenAI(
    model="deepseek-chat",  # or "deepseek-coder", "deepseek-coder:33b", etc.
    temperature=0.7,
    max_tokens=512
)

# Call the model
result = llm.invoke("What is the capital of India?")
print(result)
