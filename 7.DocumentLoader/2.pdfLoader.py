# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('7.DocumentLoader/dl-curriculum.pdf')

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)
# print(docs[1].metadata)


from langchain_docling.loader import DoclingLoader

FILE_PATH = "7.DocumentLoader/dl-curriculum.pdf"

loader = DoclingLoader(file_path=FILE_PATH)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)