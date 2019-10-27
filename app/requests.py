import urllib.request,json
from .models import RandomQuotes


api_key = None
base_url = None
popular_base_url = None

def configure_request(app):
    global api_key,base_url        
    api_key = app.config["RANDOM_API_KEY"] 
    base_url = app.config["RANDOM_BASE_URL"]
    popular_base_url = app.config["POPULAR_BASE_URL"]


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

# def get_popular_quotes():
#     '''
#     Function that gets the json response to our url reques
#     '''
    # get_popular_url = popular_base_url
    # with urllib.request.urlopen(get_popular_url) as url:

    #     get_popular_data = url.read()
    #     get_popular_response = json.loads(get_popular_data)

    #     popular_results = None

    #     if get_popular_response:

    #         popular_results_list = get_popular_response

    # return popular_results_list


