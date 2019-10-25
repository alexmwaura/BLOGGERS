import urllib.request,json
from .models import RandomQuotes

api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url        
    api_key = app.config["RANDOM_API_KEY"] 
    base_url = app.config["RANDOM_BASE_URL"]


def get_random():
    '''

    Function that gets the json response to our url request
    '''
    get_random_url = base_url
    with urllib.request.urlopen(get_random_url) as url:

        get_random_data = url.read()
        get_random_response = json.loads(get_random_data)

        random_results = None


        if get_random_response:

            random_results_list = get_random_response

            random_results = random_results_list

    return random_results
