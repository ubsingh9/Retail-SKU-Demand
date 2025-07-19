import os
import sys
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.plot_sales_tools import plot_sales_trend_tool
from src.csv_retriver import get_csv_retriever

### Setup the LLM
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

### RAG GET CSV TOOL
retriver=get_csv_retriever()

retriver_tool=create_retriever_tool(
    retriever=retriver,
    name="csv retriver",
    description="AI tools usesul to answer questions from the csv sales datasets"
)

#### List of all the tools
tools=[retriver_tool, plot_sales_trend_tool]

### Initialize Agent
agent_executer = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

