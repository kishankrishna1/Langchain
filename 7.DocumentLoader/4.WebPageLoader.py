
# --------- Sample Example of Web Page Loader ---------------------------------------------

# from langchain_community.document_loaders import WebBaseLoader

# url = 'https://docs.langchain.com/oss/python/integrations/document_loaders/index#document-loader-integrations'
# loader = WebBaseLoader(url)

# docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)


# ------------ Build Model Query from Web Page Loader ---------------------------------------------


from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-5-nano")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://docs.langchain.com/oss/python/integrations/document_loaders/index#document-loader-integrations'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)


chain = prompt | model | parser

print(chain.invoke({'question':'Give me Short Notes?', 'text':docs[0].page_content}))