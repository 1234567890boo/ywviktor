import pymongo
class Database:
    DB=None
    @staticmethod
    def initialize():
        client=pymongo.MongoClient('mongodb://127.0.0.1/')
        Database.DB=client.mydb
    @staticmethod
    def insert_record(doc):
        Database.DB.entries.insert_one(doc)
    @staticmethod
    def get_records():
        return [x for x in Database.DB.entries.find({})]
    @staticmethod
    def delete_records():
        Database.DB.entries.drop({})