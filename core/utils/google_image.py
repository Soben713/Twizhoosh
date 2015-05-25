import json
import random
import urllib.request


def get_json_response(phrase, start):
    raw_url = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&start={0}&q={1}'
    url = raw_url.format(start, urllib.request.quote(phrase))
    response = urllib.request.urlopen(url).read()
    return json.loads(response.decode('utf-8'))


def get_first_image_url_from_response(response_obj):
    return response_obj['responseData']['results'][0]['url']


def get_google_image(phrase, index):
    obj = get_json_response(phrase, index)
    return get_first_image_url_from_response(obj)


def get_random_google_image(phrase):
    r1 = get_json_response(phrase, 1)
    estimated_results = int(r1['responseData']['cursor']['estimatedResultCount'])
    # 60 is the maximum number google returns
    domain = min(60, estimated_results)
    index = random.randint(0, domain)
    r2 = get_json_response(phrase, index)
    return get_first_image_url_from_response(r2)
