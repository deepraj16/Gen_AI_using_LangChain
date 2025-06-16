from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro", 
    google_api_key="AIzaSyDH2MIUHsCK4wtHsaIK-d3cnuoFFYuLIo4"
)

response = llm.invoke("Explain how AI works in a few words")
print(response)
