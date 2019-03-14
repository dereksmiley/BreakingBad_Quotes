import requests
from requests.exceptions import HTTPError

# requests nth amount of quotes from breaking-bad-quotes
# https://github.com/shevabam/breaking-bad-quotes

def get_quotes(numQuotes):
  url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes/"
  num = str(numQuotes)
  response = requests.get(url + num)
	
  if response.status_code == 200:
      print(response.text)
  else:
      print("an error has occured : " + str(response.status_code))

