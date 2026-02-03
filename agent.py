import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

load_dotenv()

# -------- Tools --------

def calculator(expression: str) -> str:
    """Useful for solving math expressions"""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"


def text_length(text: str) -> str:
    """Returns number of characters in text"""
    return str(len(text))


tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for solving math problems"
    ),
    Tool(
        name="TextLength",
        func=text_length,
        description="Counts number of characters in text"
    ),
]

# -------- Agent --------

llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)


if __name__ == "__main__":
    while True:
        query = input("Ask agent: ")
        response = agent.run(query)
        print("Answer:", response)
