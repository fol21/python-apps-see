
###### WEB APP ########
from flask import Flask
from src.webApp.baseREST import restConfigure
import jinja2

app = Flask(__name__)


my_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader(['src/webApp/templates']),
        ])
app.jinja_loader = my_loader


restConfigure(app)

if __name__ == '__main__':
   app.run(port=8085,debug=True)




####### DATABASE #######
# import src.database.base.baseCRUD as crud

# import pymongo

# client = pymongo.MongoClient("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db")
# mydb = client["see-2018-db"]

# db = crud.createDocument(mydb, "customers",{"data":10})
# print(db)

# crudObject = crud.BaseCRUD("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db","see-2018-db")

# crudObject.updateDocument("customers",{"data":10}, {"$set":{"data":20}}).createDocument("customers",{"data":30})


