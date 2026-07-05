from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='7.DocumentLoader',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# docs = loader.load()

# print(type(docs))

# print(len(docs))


print(docs[0])

for document in docs:
    print(document.metadata)
