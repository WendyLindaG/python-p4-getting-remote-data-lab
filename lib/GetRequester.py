import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #sends a HTTP GET request to the url and stores it in response
        response= requests.get(self.url)
        #return the raw data in bytes
        return response.content
        

    def load_json(self):
        
        response= requests.get(self.url)
        #JSON DATA extracted from the response and converts it into python object
        data = response.json()
        return data
        
        

request = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
response_body = request.get_response_body()
print(response_body)

data = request.load_json()
print(data)