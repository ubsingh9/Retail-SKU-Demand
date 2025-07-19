import os
import sys
import streamlit as st
# Add root folder to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.chart_tool import plot_sales_trend
from src.query_chain import get_qa_chain
from src.agent_chain import agent_executer
st.set_page_config(page_title="Retail Q&A Assistant", layout="wide")

st.title("Retail SKU Demand Demand Assistant")
st.markdown("""
Ask any question from regarding Demand Planning. The Gen AI assistant will retrieve context and answer accurately
""")


qa_chain = get_qa_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

user_query=st.chat_input("Ask about sales trends, stock-outs, SKUs...")
if user_query:
    with st.spinner("Thinking..."):
        result = qa_chain.invoke(user_query)
        st.session_state.chat_history.append((user_query, result))
    
# Display history
for query, response in st.session_state.chat_history:
    st.chat_message("user").write(query)
    st.chat_message("assistant").markdown(response)