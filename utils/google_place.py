import json

import googlemaps
import requests

from utils.util import log

api_key = 'AIzaSyCDcUmm1LO0yeRVqdPsxo2ku6-weisiWHk'


def search_place(place='Museum of Contemporary Art Australia'):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=place_id&key={}".format(place, api_key)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


def search_phone(place_id='ChIJm7NJkla3j4AR8vR-HWRxgOo'):
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=formatted_phone_number&key={}".format(place_id, api_key)

    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        # if response.text['status'] == 'OK':
        if response.ok:
            text = json.loads(response.text)
            result = text['result']
            phone_number = result['formatted_phone_number']
            print(text)
            print(phone_number)
            return phone_number
        return None
        # print(response.text)
    except Exception as e:
        print(e.__str__())
        return None
        # log(e.__str__())


if __name__ == '__main__':
    # search_place(place='Museum of Contemporary Art Australia')
    # search_place(place='Computer History Museum Mountain View')
    search_phone(place_id='ChIJm7NJkla3j4AR8vR-HWRxgOo')
