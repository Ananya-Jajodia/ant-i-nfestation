# from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_ollama import OllamaEmbeddings
# from langchain.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama

import pickle
import faiss

embeddings = OllamaEmbeddings(model="nomic-embed-text")
faiss_index = faiss.read_index("faiss_index.bin")

# Load document metadata
with open("faiss_metadata.pkl", "rb") as f:
    documents = pickle.load(f)

# Create Docstore & ID Mapping
docstore = InMemoryDocstore()
index_to_docstore_id = {}
for i, doc in enumerate(documents):
    doc_id = str(i)
    docstore.add({doc_id: doc})  # Store the document with its ID
    index_to_docstore_id[i] = doc_id  # Map index positions to IDs

# Reconstruct FAISS vector store properly
vector_db = FAISS(
    embedding_function=embeddings,
    index=faiss_index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5})


# Set up a retrieval chain
retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=Ollama(model="llama3.2"),
    retriever=vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
    memory=memory
)

# queries = [
#     "How much water do my daylilies need?",
#     "How much sun do my daylilies need?",
#     "What time of year should I fertilize my daylilies?"
# ]

# for query in queries:
#     results = vector_db.similarity_search(query, k=3)  # Retrieve top 3 results
#     print(f"\n🔍 Query: {query}")
#     for i, doc in enumerate(results):
#         print(f"Result {i+1}: {doc.page_content}")

print(vector_db.similarity_search("How much water do my daylilies need?")[0].page_content)
print(vector_db.similarity_search("How much sun does it need?")[0].page_content)
print(vector_db.similarity_search("What time of year should I fertilize it?")[0].page_content)

# for i, doc in enumerate(results):
#     print(f"Result {i+1}: {doc.page_content}")