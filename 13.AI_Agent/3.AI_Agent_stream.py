from dotenv import load_dotenv
load_dotenv()

from rich import print # for better printing

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.messages import AIMessageChunk
import requests
from tavily import TavilyClient 
tavily_client = TavilyClient()


# -------------------Tools------------------------------------

@tool
def get_weather(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=57821ed4455b5299f0fd9f45cb6ffa9c&query={city}'

  response = requests.get(url)

  return response.json()

@tool
def get_news(city:str) -> str:
    """ Get the Latest news about the city """

    response = tavily_client.search(
        query=f"Latest news about {city}",
        topic="news",
        search_depth="basic",
        max_results=3
    )
    return response


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    streaming=True
)

agent = create_agent(
    model=llm,
    tools=[get_news, get_weather],
    system_prompt="""
    You are a helpful city assistant.
    Use available tools whenever necessary to answer user questions.
    """
)


messages = []

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content=user_input))

    print("\nAI: ", end="", flush=True)

    final_state = None

    for mode, data in agent.stream(
        {"messages": messages},
        stream_mode=["messages", "values"],
    ):
        if mode == "messages":
            message, metadata = data

            if isinstance(message, AIMessageChunk):
                print(message.content, end="", flush=True)

        elif mode == "values":
            final_state = data

    if final_state:
        messages = final_state["messages"]

    print("\n","*"*100, "\n")


