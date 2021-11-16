"""
Date: 16.11.2021
"""
import json
import requests

import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    response = requests.get(url)
    top_artists = json.loads(response.text)
    return top_artists['topartists']['artist'][0]['name']


url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=0a5de916777ad83d6de29347308556a1&format=json'
api_get_request(url)
