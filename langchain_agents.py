##Updated langchain code
from langchain_openai import ChatOpenAI  # Use ChatOpenAI instead of OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv

load_dotenv()

def standalone_langchain_agent():
    # 1. Use ChatOpenAI (it follows logic better than the legacy OpenAI class)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # 2. Keep your tools
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    # 3. Initialize the agent
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True,
        handle_parsing_errors=True # Added this to handle formatting issues
    )

    # 4. Run with a clear request
    result = agent.run(
        "Find the average lifespan of a dog on Wikipedia. Take that number and multiply it by 3."
    )

    print(result)

if __name__== "__main__":
    standalone_langchain_agent()
