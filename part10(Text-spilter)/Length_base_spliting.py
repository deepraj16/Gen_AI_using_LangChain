from langchain.text_splitter import CharacterTextSplitter 
from dotenv import load_dotenv 
from langchain_community.document_loaders import PyPDFLoader 


load_dotenv()

text = """
4.1.Data Collection and Preprocessing
Data preprocessing is a critical step in the data analysis and machine learning workflow, involving various techniques to prepare raw data for further analysis. This process aims to clean, transform, and organize the data to enhance its quality and ensure it is suitable for modelling . Here are key aspects of data preprocessing:
Steps of Data Preprocessing
Data preprocessing is an important step in the data mining process that involves cleaning and transforming raw data to make it suitable for analysis. Some common steps in data preprocessing include:
1.	Data Cleaning: This involves identifying and correcting errors or inconsistencies in the data, such as missing values, outliers, and duplicates. Various techniques can be used for data cleaning, such as imputation, removal, and transformation.
2.	Data Integration: This involves combining data from multiple sources to create a unified dataset. Data integration can be challenging as it requires handling data with different formats, structures, and semantics. Techniques such as record linkage and data fusion can be used for data integration.
3.	Data Transformation: This involves converting the data into a suitable format for analysis. Common techniques used in data transformation include normalization, standardization, and discretization. Normalization is used to scale the data to a common range, while standardization is used to transform the data to have zero mean and unit variance. Discretization is used to convert continuous data into discrete categories.
4.	Data Reduction: This involves reducing the size of the dataset while preserving the important information. Data reduction can be achieved through techniques such as feature selection and feature extraction. Feature selection involves selecting a subset of relevant features from the dataset, while feature extraction involves transforming the data into a lower-dimensional space while preserving the important information.
5.	Data Discretization: This involves dividing continuous data into discrete categories or intervals. Discretization is often used in data mining and machine learning algorithms that require categorical data. Discretization can be achieved through techniques such as equal width binning, equal frequency binning, and clustering.
Cyber Threats: An Overview
Cyber threats refer to any malicious attempt by individuals, groups, or organizations to damage, disrupt, steal, or gain unauthorized access to computer systems, networks, or data. As digital technology continues to evolve and permeate every aspect of modern life, cyber threats have become a critical concern for individuals, businesses, and governments worldwide. Cyber threats can take many forms and often exploit vulnerabilities within systems or manipulate human behavior to achieve their goals.
Here’s an in-depth look at what cyber threats are, their types, methods, and the impact they can have:
1. Types of Cyber Threats
•	Malware: Short for "malicious software," malware includes viruses, worms, trojans, spyware, and ransomware designed to damage or gain unauthorized access to a system. Malware can spread through infected files, applications, or websites.
•	Phishing: A type of social engineering attack, phishing involves tricking individuals into sharing sensitive information, such as passwords or credit card numbers. Attackers often use emails or fake websites that mimic legitimate ones to deceive victims.
•	Ransomware: This is a specific form of malware that encrypts a victim's data, making it inaccessible until a ransom is paid to the attacker. Ransomware attacks have increased dramatically, affecting both individuals and large organizations.
•	DDoS (Distributed Denial of Service) Attacks: In a DDoS attack, multiple compromised devices flood a target system or network with excessive traffic, causing it to slow down or crash. These attacks aim to disrupt normal services, often to create chaos or extort a ransom.
•	Insider Threats: These threats come from within an organization, often by employees or former employees who have access to sensitive information. Insider threats can be difficult to detect, as they exploit trusted access within a network.
•	Advanced Persistent Threats (APTs): APTs are prolonged and targeted cyberattacks, often orchestrated by well-funded and sophisticated attackers. They focus on infiltrating high-value targets, such as government agencies or multinational corporations, and often go undetected for long periods.

"""

loader = PyPDFLoader("path")
doc=loader.load()

spliter = CharacterTextSplitter( 
    chunk_size=100, 
    chunk_overlap=10, 
    separator=''
)

spit=spliter.split_text(text)
spit2=spliter.split_documents(doc)
print(spit[0])