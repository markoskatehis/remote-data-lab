import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url
        self.response = None

    def get_response_body(self):
        try: 
            res = requests.get(self.url)
            res.raise_for_status()
            self.response = res
            return res.content
        except requests.RequestException as e:
            print(f"Error fetching data from {self.url}: {e}")
            return None

    def load_json(self):
        if self.response is None:
            self.get_response_body()

        if self.response is None:
            return None
        
        try:
            return self.response.json()
        except ValueError as e:
            print (f"Error parsing JSON: {e}")
            return None