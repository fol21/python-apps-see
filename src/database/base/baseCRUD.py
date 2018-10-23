import pymongo


def createCollection(name):
    client = pymongo.MongoClient("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db")
    mydb = client["see-2018-db"]

    mycol = mydb[name]
    
    return mydb
    




