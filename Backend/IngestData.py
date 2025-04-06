import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from gemini_embeddings import GeminiEmbeddings

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
chroma_db_path = os.getenv('CHROMA_DB_PATH')

documents = [
    Document(page_content='Meeting notes: Discuss project X deliverables'),
    Document(page_content='Reminder: Submit report by Friday'),
    Document(page_content='Upcoming event: Tech Conference next Wednesday')
]

textSplitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
chunks = textSplitter.split_documents(documents=documents)

embeddings = GeminiEmbeddings(api_key=google_api_key) 

vectorDB = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=chroma_db_path)

print('Documents successfully indexed')