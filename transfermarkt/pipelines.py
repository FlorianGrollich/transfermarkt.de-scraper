import pymongo


class TransfermarktPipeline(object):
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['transfermarkt_db']  # Database name
        self.collection = self.db['matches']  # Collection name
        self.collection.insert_one({"test": "connection"})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
