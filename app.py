from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

# ✅ Read token
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise ValueError("❌ Token not loaded from .env file.")

# ✅ Initialize client with a working model
client = InferenceClient(
    model="tiiuae/falcon-7b-instruct",  # working inference model
    token=token
)

# ✅ Make a request
response = client.text_generation(
    prompt="What is artificial intelligence?",
    max_new_tokens=50
)

print(response)
