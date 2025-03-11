from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import LlamaCppEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import numpy as np
 

def normalize(vectors):
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


loader = CSVLoader(file_path="/Users/MikaFinkman/cs4701/ant-i-nfestation/backend/chatbot/daylilies_data.csv")
documents = loader.load()
document_texts = [doc.page_content for doc in documents]
embeddings = OllamaEmbeddings(model="llama3.2")
vectors = embeddings.embed_documents(document_texts)
vectors = normalize(np.array(vectors))
vector_db = FAISS.from_documents(documents, embeddings, normalize_L2=True)
# vector_db = FAISS.from_documents(documents, embeddings)

# print(vector_db.similarity_search("How much water do my daylilies need?")[1].page_content)
print(vector_db.similarity_search("How much sun do my daylilies need?"))

# print(documents)




