# from sentence_transformers import SentenceTransformer



# documents = [
#     {"id": 1, "text": "Tài liệu thứ nhất"},
#     {"id": 2, "text": "Tài liệu thứ hai"},
#     # Thêm các tài liệu khác
# ]

# # Sử dụng mô hình nhúng để chuyển văn bản thành vector




# class Embedding:

#     def __init__(self) -> None:
#         self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

#     def embed(self, documents):
#         document_texts = [doc["text"] for doc in documents]
#         document_vectors = self.model.encode(document_texts)