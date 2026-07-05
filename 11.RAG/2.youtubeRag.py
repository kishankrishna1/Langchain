from dotenv import load_dotenv
import os

load_dotenv()

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

def getTranscript(video_id):

    api = YouTubeTranscriptApi() 
    try:
        fetched = api.fetch(video_id, languages=["en"])
        transcript = " ".join(chunk.text for chunk in fetched)  # .text not ["text"]
        # print(transcript)
        return transcript

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"No captions available: {e}")
        return None

    
video_id = "Gfr50f6ZBvo" # only the ID, not full URL
transcript = getTranscript(video_id)
if not transcript:
    raise ValueError("Could not fetch transcript. Exiting.")


# Indexing (Text splitters)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])


# Embedding Generation and vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="rag_chroma_db" )


# Retriver
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text


# Augmentation
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)


# Building a Chains
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

response = main_chain.invoke("Can you summarize the video?")
print(response)

