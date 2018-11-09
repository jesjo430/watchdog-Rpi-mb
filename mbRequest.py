import requests 
import json
mb_endpoint = "https://megabeta.se/rasp_endpoint"

def send(source, data, url=mb_endpoint):
    temp = "{'" + source + "'" + ": '" + data + "'}" 
    r = requests.post(url, params=temp)

    if r.status_code != 200:
        print ("Error: ", r.status_code)

    print(r.json())

    return r.status_code