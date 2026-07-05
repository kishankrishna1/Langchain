
# ----------- For Single Sentence --------------------------

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))


# ---------- For Complete Documents---------------------------

# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# documents = [
#     "Delhi is the capital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris is the capital of France"
# ]

# result = embedding.embed_documents(documents)

# print(str(result))

# ----------For Testing Purpose---------------------------------

# ----------------FakeEmbeddings integration----------------
# LangChain also provides a fake embedding class. You can use this to test your pipelines.

# from langchain_community.embeddings import FakeEmbeddings

# embeddings = FakeEmbeddings(size=10)

# query_result = embeddings.embed_query("woooooo")

# print(query_result)

# doc_results = embeddings.embed_documents(["woooooo", "hahahaaa"])

# print(doc_results)
