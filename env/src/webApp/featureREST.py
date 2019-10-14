import base64
from ..computer_vision.RESTConfig import *
from ..database.features.featureCRUD import FeatureCRUD
from flask import render_template, request, jsonify

from .baseREST import baseREST


def featureREST(app, vision_base_url, subscription_key):
    baseREST(app)
    dataAccess = FeatureCRUD('mongodb://admin:see2019@ds035747.mlab.com:35747/see-db-2019?retryWrites=false','see-db-2019')

    @app.route('/api/feature/insert',methods = ['POST'])
    def insert():
        data = request.json
        image_data = base64.b64decode(data['base64'])
        analysis = analyze(
            data=image_data,
            credentials={'base_url': vision_base_url, 'subscription_key': subscription_key},
            features_list=['Categories', 'Description', 'Color'])
        dataAccess.insertAnalysis(data['name'], data['base64'], analysis)
        return 'ok'
