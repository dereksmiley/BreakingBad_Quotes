import requests
import json
from requests.exceptions import HTTPError

# requests nth amount of quotes from breaking-bad-quotes
# https://github.com/shevabam/breaking-bad-quotes

def get_quotes(numQuotes):
  url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes/"
  num = str(numQuotes)
  response = requests.get(url + num)
	
  if response.status_code == 200:
    data = response.text
    json_obj = json.loads(data)
    for obj in json_obj:
      print(obj['quote'] + "  - " + obj['author'] + '\n')
  
  else:
    print("an error has occured : " + str(response.status_code))