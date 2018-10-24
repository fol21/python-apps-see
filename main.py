import src.database.base.baseCRUD as crud

import pymongo

client = pymongo.MongoClient("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db")
mydb = client["see-2018-db"]

db = crud.createDocument(mydb, "customers",{"data":10})
print(db)

crudObject = crud.BaseCRUD("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db","see-2018-db")

crudObject.updateDocument("customers",{"data":10}, {"$set":{"data":20}}).createDocument("customers",{"data":30})


