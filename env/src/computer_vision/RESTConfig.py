import requests

def analyze(credentials, data, features_list):
    headers = {'Ocp-Apim-Subscription-Key': credentials['subscription_key'],
           'Content-Type': 'application/octet-stream'}
    visualFeatures = ','
    params = {'visualFeatures': visualFeatures.join(features_list)}
    response = requests.post(
        credentials['base_url'] + '/vision/v2.0/analyze',
        headers=headers,
        params=params,
        data=data
    )
    response.raise_for_status()
    return response.json()


def detect(credentials, data):
    headers = {'Ocp-Apim-Subscription-Key': credentials['subscription_key'],
           'Content-Type': 'application/octet-stream'}
    response = requests.post(
        credentials['base_url'] + '/vision/v2.0/detect',
        headers=headers,
        data=data
    )
    response.raise_for_status()
    return response.json()

def ocr(credentials, data, language='pt', detect_orientation=True):
    headers = {'Ocp-Apim-Subscription-Key': credentials['subscription_key'],
           'Content-Type': 'application/octet-stream'}
    params = {
              'language': language,
              'detectOrientation': detect_orientation
             }
    response = requests.post(
        credentials['base_url'] + '/vision/v2.0/ocr',
        headers=headers,
        params=params,
        data=data
    )
    response.raise_for_status()
    return response.json()