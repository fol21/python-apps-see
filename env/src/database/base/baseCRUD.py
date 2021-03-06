import pymongo


def createDocument(db, collection, document):
    mycol = db[collection]
    mycol.insert_one(document)
    return db

def readDocument(db, collection, query):
    mycol = db[collection]
    return mycol.find(query)

def updateDocument(db, collection, query, values):
    mycol = db[collection]
    mycol.update_one(query, values)
    return db

def deleteDocument(db,collection, query):
    mycol = db[collection]
    mycol.delete_one(query)
    return db

class BaseCRUD:
    
    def __init__(self,url,dbname):
        self.db = pymongo.MongoClient(url)[dbname]
        self.response = None


    def createDocument(self, collection, document):
        mycol = self.db[collection]
        mycol.insert_one(document)
        return self

    def readDocument(self, collection, query):
        mycol = self.db[collection]
        return mycol.find(query)

    def updateDocument(self, collection, query, values):
        mycol = self.db[collection]
        mycol.update_one(query, values)
        return self

    def deleteDocument(self,collection, query):
        mycol = self.db[collection]
        mycol.delete_one(query)
        return self 
    




