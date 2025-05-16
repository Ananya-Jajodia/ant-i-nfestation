from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import pickle
import faiss

loader = CSVLoader(file_path="/Users/MikaFinkman/cs4701/ant-i-nfestation/backend/chatbot/transformed_plant_data.csv")
documents = loader.load()
document_texts = [doc.page_content for doc in documents]
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectors = embeddings.embed_documents(document_texts)
vector_db = FAISS.from_documents(documents, embeddings, normalize_L2=True)

faiss.write_index(vector_db.index, "faiss_index.bin")
with open("faiss_metadata.pkl", "wb") as f:
    pickle.dump(documents, f)






