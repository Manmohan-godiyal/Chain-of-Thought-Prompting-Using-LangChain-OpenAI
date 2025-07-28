import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

# Load your API key securely
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Use ChatPromptTemplate for GPT-3.5
prompt = ChatPromptTemplate.from_template("""
Answer the following question with a step-by-step explanation:
Question: {question}
Let's think step by step.
""")

# Use GPT-3.5-turbo model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Chain using | operator
chain: Runnable = prompt | llm

# Ask a question
question = "If a car travels at 70 km/h for 2 hours, how far does it go?"
response = chain.invoke({"question": question})

# Print the model's response
print(response.content)
