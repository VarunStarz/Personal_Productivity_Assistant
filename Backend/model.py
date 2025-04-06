import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.chains import retrieval_qa
from langchain.chains.question_answering import load_qa_chain
from .gemini_embeddings import GeminiEmbeddings

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
chroma_db_path = os.getenv('CHROMA_DB_PATH')

embeddings = GeminiEmbeddings(api_key=google_api_key) 
vectorDB = Chroma(embedding_function=embeddings, persist_directory=chroma_db_path)
retriever = vectorDB.as_retriever()

from langchain_google_genai import ChatGoogleGenerativeAI
geminiLLM = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.3, google_api_key=google_api_key)

qaChain = load_qa_chain(llm=geminiLLM, chain_type='stuff')

def getResponse(query):
    print('Entering into model getResponse')
    relevantDocuments = retriever.get_relevant_documents(query=query)
    print(f'relevantDocuments ---> {relevantDocuments}')
    print('Returning from model getResponse')
    return qaChain.run({'input_documents': relevantDocuments, 'question': query})

print('model.py done')