from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()
import streamlit as st

# GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
#os.environ["GROQ_API_KEY"] = GROQ_API_KEY

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

def load_vectorstore(path = 'vectorstore_csv'):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

def get_qa_chain():
    vectorstore=load_vectorstore()
    retrieval = vectorstore.as_retriever(search_kwars={"k":4})

    llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model="llama-3.1-8b-instant", temperature=0.2)

    prompt_template = """
    You are a demand planning expert assistant. Based on the context from retail sales and inventory data,
    answer the user query in a professional, analytical way. If relevant, return structured output (e.g., markdown table or list).

    CONTEXT:
    {context}

    QUESTION:
    {question}

    Helpful Answer:
    """
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template
    )

    # Create the RetrievalQA chain using FROM_CHAIN_TYPE
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retrieval,
        chain_type="stuff",  # Correct usage here
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )

    return qa_chain

if __name__=="__main__":
    qa_chain = get_qa_chain()
    query = "Why is SKU_5678 underperforming in East region?"
    result = qa_chain.invoke({"query":query})
    print(result['result'])
