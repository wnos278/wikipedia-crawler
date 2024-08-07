import os 
from src.opensearchlib import * 
from src.embedding import * 

from dotenv import load_dotenv
load_dotenv()


class IndexDocument:

    def __init__(self) -> None:
        self.db = OpenSearchDB(index_name=os.getenv('INDEX_NAME'), 
                               host=os.getenv('ADDRESS'), 
                               port=os.getenv('PORT'), 
                               username=os.getenv('USERNAME'), 
                               password=os.getenv('PASSWORD'))
        # self.embed_model = Embedding() 

        
    def chunk_document(self):
        chunks = []
        # NOTE: Chia thanh y 

        # NOTE: Tra ve 1 list cac y 

        return chunks

    def index_document(self, document):
        id = "" 
        body = {
            'link': document['link'],
            'content': document['content']
            }
        
        result = self.db.opensearch_index(id=id, body=body)
        if not result:
            return -1
        else:
            return 1 
        
    def update_document(self, document):
        id = document['id']
        # Lay body cua document 
        embedding_vector = self.embed_model.embed(document['content'])

        update_body = {
            'embedding_vector': embedding_vector,
            }
    