# This python script handles news api request
#created 4/19/2020
# Last Updated: 4/19/2020
# Credits:nóto

import news.nyt.handler as nyt
nyt = nyt.NewsApi()
import news.org.handler as org
org = org.NewsApi()


def newsQuery(ticker):
  #get org query and store as json
  org_json = org.autoQuery(ticker, 'en')
  #get nyt query and store as json
  nyt_json = nyt.autoQuery(ticker)

  formated_json = { 
            'articles': org_json['articles'] + nyt_json['articles']
  }

  formated_json['articles'].sort(key=lambda x:x['timestamp'])
  #reverse list so we can see the latest news first
  formated_json['articles'] = list(reversed(formated_json['articles']))
  return(formated_json)
