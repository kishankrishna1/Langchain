from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='./7.DocumentLoader/social_network.csv')

docs = loader.load()

print(len(docs))
print(docs[1])
print(docs[2])
