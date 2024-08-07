from opensearchpy import OpenSearch
from opensearchpy.helpers import scan 


class OpenSearchDB:

    def __init__(self, index_name, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.index_name = index_name
        self.client = None 

        self.opensearch_connect() 


    def opensearch_connect(self):
        self.client = OpenSearch(
            hosts = [{'host': self.host, 'port': self.port}],
            http_compress = True, 
            http_auth = (self.username, self.password),
            use_ssl = True,
            verify_certs = False,
            ssl_assert_hostname = False,
            ssl_show_warn = False,
        )
        body = {"mappings": {"dynamic": "true"}}
        is_existed = self.client.indices.exists(index=self.index_name)
        print(is_existed)
        try:
            
            self.client.indices.get(index=self.index_name)
        except:
            self.client.indices.create(index=self.index_name, body=body)


    def opensearch_index(self, id, body):
        try:
            response = self.client.index(    
                index=self.index_name,
                body=body,
                id=id,
                refresh=True
            )
            return True
        except Exception as ex:
            print(ex)
            return False
            

    def opensearch_get_doc(self, doc_id):
        try:
            return self.client.get(self.index_name, doc_id)
        except:
            return []

    def opensearch_get_all_documents(self):
        documents = []
        docs = scan(self.client,
                     query={"query": {"match_all": {}}},
                     index=self.index_name,
                     scroll='5m',
                     size=1000)

        for document in docs:
            documents.append(document)

        return documents
    
    def check_document_exists(self, document_id):
        try:
            response = self.client.exists(index=self.index_name, id=document_id)
            return not response 
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def opensearch_reset_index(self):
        try:
            self.client.indices.delete(index=self.index_name)
        except:
            return 

        body = {"mappings": {"dynamic": "true"}}
        self.client.indices.create(index=self.index_name, body=body)

    def dbbackup(self):
        pass 

    def close(self):
        self.client.close()