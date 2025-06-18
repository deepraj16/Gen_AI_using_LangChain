from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise ValueError(" Token not loaded from .env file.")

client = InferenceClient(
    model="tiiuae/falcon-7b-instruct",  # working inference model
    token=token
)

response = client.text_generation(
    prompt="What is artificial intelligence?",
    max_new_tokens=50
)

print(response)
