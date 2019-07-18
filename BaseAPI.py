import requests

def get_api_root():
    """Return the api root"""
    return "https://swapi.co/api/"

def return_api_json(requested_url):
    """Return the 'requested_url' response in json format"""
    r = requests.get(url = requested_url)
    r.raise_for_status()
    return r.json()
