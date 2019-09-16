
###### WEB APP ########
# from flask import Flask
# from src.webApp.baseREST import restConfigure
# import jinja2


# app = Flask(__name__)


# my_loader = jinja2.ChoiceLoader([
#             app.jinja_loader,
#             jinja2.FileSystemLoader(['src/webApp/templates']),
#         ])
# app.jinja_loader = my_loader


# restConfigure(app)

# if __name__ == '__main__':
#    app.run(port=8085,debug=True)




####### DATABASE #######
# import src.database.base.baseCRUD as crud

# import pymongo

# client = pymongo.MongoClient("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db")
# mydb = client["see-2018-db"]

# db = crud.createDocument(mydb, "customers",{"data":10})
# print(db)

# crudObject = crud.BaseCRUD("mongodb://administrador:see2018@ds027748.mlab.com:27748/see-2018-db","see-2018-db")

# crudObject.updateDocument("customers",{"data":10}, {"$set":{"data":20}}).createDocument("customers",{"data":30})


#### Computer Vision ####

import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
from PIL import Image
from io import BytesIO
import json

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "9d5a6f15631142808a154f9916f0880a"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westcentralus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://fol-computer-vision.cognitiveservices.azure.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.
image_path = "C:\\Users\\fol\\Downloads\\dog.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()
analysis = response.json()
print(json.dumps(analysis, indent=1))