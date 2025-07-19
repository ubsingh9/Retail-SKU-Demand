import importlib.util
import sys
import os
import streamlit as st
# Ensure src folder is in sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Then do the import
from src.agent_chain import agent_executer

st.set_page_config(page_title="Agentic Retail Assistant", layout="wide")
st.title("🛒 Agentic Retail SKU Demand Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.chat_input("Ask your question...")

if query:
    st.chat_message("user").write(query)
    with st.spinner("Agent thinking..."):
        try:
            result = agent_executer.run(query)

            # Save history
            st.session_state.chat_history.append((query, result))

            # Show assistant reply
            st.chat_message("assistant").markdown(
                result["output"] if isinstance(result, dict) and "output" in result else result
            )

            # Show chart if image path is returned
            if isinstance(result, dict) and str(result.get("output", "")).endswith(".png"):
                st.image(result["output"], caption="Generated Chart")

        except Exception as e:
            st.error(f"Agent failed: {str(e)}")

# Show previous conversation
for user_msg, bot_msg in st.session_state.chat_history:
    st.chat_message("user").write(user_msg)
    st.chat_message("assistant").markdown(bot_msg)
