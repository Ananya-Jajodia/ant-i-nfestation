# # from langchain_community.document_loaders.csv_loader import CSVLoader
# from langchain_ollama import OllamaEmbeddings
# # from langchain.llms import Ollama
# from langchain_community.vectorstores import FAISS
# from langchain_community.docstore.in_memory import InMemoryDocstore
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
# from langchain_community.llms import Ollama
# from langchain.chains.question_answering import load_qa_chain
# from langchain.chains.llm import LLMChain
# from langchain.prompts import PromptTemplate

# import pickle
# import faiss

# embeddings = OllamaEmbeddings(model="nomic-embed-text")
# faiss_index = faiss.read_index("faiss_index.bin")

# # Load document metadata
# with open("faiss_metadata.pkl", "rb") as f:
#     documents = pickle.load(f)

# # Create Docstore & ID Mapping
# docstore = InMemoryDocstore()
# index_to_docstore_id = {}
# for i, doc in enumerate(documents):
#     doc_id = str(i)
#     docstore.add({doc_id: doc})  # Store the document with its ID
#     index_to_docstore_id[i] = doc_id  # Map index positions to IDs

# # Reconstruct FAISS vector store properly
# vector_db = FAISS(
#     embedding_function=embeddings,
#     index=faiss_index,
#     docstore=docstore,
#     index_to_docstore_id=index_to_docstore_id
# )

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# # Set up a retrieval chain
# retrieval_chain = ConversationalRetrievalChain.from_llm(
#     llm=Ollama(model="llama3.2"),
#     retriever=vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
#     memory=memory
# )

# queries = [
#     "How much water does my roses need?",
#     "How much sun do they need?",
#     "What time of year should I fertilize them?"
# ]

# for query in queries:
#     result = retrieval_chain.run(query)
#     print(result)

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import faiss
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama

app = Flask(__name__)
CORS(app)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
faiss_index = faiss.read_index("faiss_index.bin")

with open("faiss_metadata.pkl", "rb") as f:
    documents = pickle.load(f)

docstore = InMemoryDocstore()
index_to_docstore_id = {}
for i, doc in enumerate(documents):
    doc_id = str(i)
    docstore.add({doc_id: doc})
    index_to_docstore_id[i] = doc_id

vector_db = FAISS(
    embedding_function=embeddings,
    index=faiss_index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=Ollama(model="llama3.2"),
    retriever=vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
    memory=memory
)

@app.route('/api/plant-chat', methods=['POST'])
def plant_chat():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    result = retrieval_chain.run(query)
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
