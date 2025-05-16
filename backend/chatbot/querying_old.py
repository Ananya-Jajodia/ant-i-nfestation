from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

import pickle
import faiss

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

queries = [
    "How much water does my roses need?",
    "How much sun do they need?",
    "What time of year should I fertilize them?"
]

for query in queries:
    result = retrieval_chain.run(query)
    print(f"\nUser: {query}\nBot: {result}")