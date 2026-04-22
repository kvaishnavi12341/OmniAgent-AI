from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings()
        self.db = None

    def build(self, docs):
        self.db = FAISS.from_texts(docs, self.embedding)

    def search(self, query):
        if self.db:
            return self.db.similarity_search(query)
        return []