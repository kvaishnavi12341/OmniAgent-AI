class Retriever:
    def __init__(self, vector_store):
        self.vs = vector_store

    def retrieve(self, query):
        results = self.vs.search(query)
        return [doc.page_content for doc in results]