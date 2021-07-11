from bs4 import BeautifulSoup
import requests

class webScraper():
   def __init__(self):
      self.headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '3600',
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
      }
      self.html_return_string = ""
   def scrape(self):
      r = requests.get('https://www.google.com/search?client=firefox-b-1-d&q=search+engiens')
      data = r.text
      soup = BeautifulSoup(data, features='lxml')
      soup.prettify()
      for link in soup.find_all('cite'):
         self.html_return_string = self.html_return_string + str(link.get_text())
      self.html_return_string = str("<div>" + self.html_return_string + "</div>")
      return str(self.html_return_string)

      
         