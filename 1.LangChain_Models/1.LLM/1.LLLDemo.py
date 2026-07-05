# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI(model="gpt-5-nano")

# result = llm.invoke("what is the capital of India")

# print(result)

# ---------------------------------------------------------------

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# result = llm.invoke("what is the capital of India")
# print(result)

# -----------------------------------------------------------------

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

result = llm.invoke("what is the capital of India")

print(result)