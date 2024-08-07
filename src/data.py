from datetime import datetime, date
FORMAT_TIME = "%Y/%m/%d %H:%M:%S"
class Post:
    def __init__(self):
        self.Bot_id=0
        self._id = ""
        self.type="wikipedia"
        self.title = ""
        self.link = "" 
        self.crawled_time = datetime.now().strftime(FORMAT_TIME) 
        self.content = "" 
