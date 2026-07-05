from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

result = model.invoke("what is the capital of India")

print(result)

# ---------------------------------------------------------------

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# result = model.invoke("what is the capital of India")
# print(result)

# -----------------------------------------------------------------

# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(model="llama-3.3-70b-versatile")

# result = model.invoke("what is the capital of India")

# print(result)

# print(result.content)