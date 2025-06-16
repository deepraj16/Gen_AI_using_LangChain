import langchain 
import transformers

from langchain import HuggingFaceHub
print(langchain.__version__)

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.5, "max_length": 100}
)

response = llm("Explain LangChain in one sentence.")
print(response)


gemin_key="AIzaSyCEBhovdE6nwDvL2YMIGkUpQsETX616vR8"