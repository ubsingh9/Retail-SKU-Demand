import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from chunk_csv_rows import load_and_chunk_csv
from tqdm import tqdm
from langchain.docstore.document import Document

def generate_embeddings(file_path):

    print(f'inside generate embeddings')
    chunks = load_and_chunk_csv(file_path)
    print(f'chunking is done')
    chunks=chunks[:50000]
    

    # initialized embedding models
    embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print(f'embedding is done')

    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    print(f'Vector store creation is done')
    vectorstore.save_local("vectorstore_csv/")
    print(f'Embedding {len(chunks)} chunks are saved  to vectorstore')


if __name__ == "__main__":
    file_path="data/retail_store_inventory.csv"
    generate_embeddings(file_path)