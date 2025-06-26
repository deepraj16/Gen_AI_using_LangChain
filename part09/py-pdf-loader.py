from langchain_community.document_loaders import PyPDFLoader 
import os 

loader= PyPDFLoader( "Deepraj_Resume (7).pdf")
doc=loader.load()

print(doc)