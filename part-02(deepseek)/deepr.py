from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Directly set your token here
HUGGINGFACE_API_TOKEN = "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"

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACE_API_TOKEN,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")
print(response.content)
