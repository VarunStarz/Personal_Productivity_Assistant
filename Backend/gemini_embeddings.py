from langchain.embeddings.base import Embeddings
from google.genai import Client

class GeminiEmbeddings(Embeddings):
    def __init__(self, api_key):
        self.client = Client(api_key=api_key)

    def embed_documents(self, documents):
        # Generate embeddings for a list of documents
        results = self.client.models.embed_content(
            model="models/text-embedding-004",
            contents=documents
        )
        return [embedding.values for embedding in results.embeddings]
        #return results.embeddings

    def embed_query(self, query):
        # Generate embedding for a single query
        result = self.client.models.embed_content(
            model="models/text-embedding-004",
            contents=query
        )
        #return result['embedding']
        return result.embeddings[0].values