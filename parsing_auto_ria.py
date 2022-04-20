import requests
from bs4 import BeatifulSoup


#url 
url = 'https://auto.ria.com/uk/newauto/'
HEADERS = {'user-agent': 'user-agent', 'accept': '*/*'} # the your user-agent

def get_html(url, params = None):
  r = requests.get(url, headers = HEADERS, params = params)
  return r

def parse():
  html = get_html(url)
  if html.status_code = 200:
    pass
  else:
    print('error')
    
  get_html()
  
if __name__ == "__main__":
  parse()
  

