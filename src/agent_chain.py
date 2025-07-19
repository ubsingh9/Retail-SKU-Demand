import os
import sys
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import streamlit as st
#GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
#os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.plot_sales_tools import plot_sales_trend
from src.csv_retriver import get_csv_retriever

# LLM Setup
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),temperature=0.2, model="llama3-8b-8192")

# Retriever Setup
vectorstore = get_csv_retriever()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 🧠 WRAPPED RETRIEVER TOOL – returns plain text!
def csv_retriever_func(query: str) -> str:
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs])  # Only return text

# 📦 Create LangChain Tool (manually)
csv_retriever_tool = Tool(
    name="csv_retriever",
    func=csv_retriever_func,
    description="Use this to answer general questions about sales, inventory, pricing. Do not use for chart plotting."
)

plot_sales_trend_tool = Tool(
    name="plot_sales_trend_tool",
    func=plot_sales_trend,
    description="Use this to plot sales trends of a specific Product ID (SKU). Requires SKU and optionally Region."
)


# 📈 Add other tools
tools = [csv_retriever_tool, plot_sales_trend_tool]

# 🤖 Agent Initialization
agent_executer = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

__all__ = ["agent_executer"]