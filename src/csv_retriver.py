from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_csv_retriever():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("vectorstores_csv", embeddings=embedding, allow_dangerous_deserialization=True)
    return vectorstore.as_retriever()

