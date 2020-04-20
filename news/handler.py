# This python script handles news api request
#created 4/19/2020
# Last Updated: 4/19/2020
# Credits:nóto

import nyt.handler as nyt
nyt = nyt.NewsApi()
import org.handler as org
org = org.NewsApi()


def newsQuery(ticker):
  #get org query and store as json
  org_json = org.autoQuery(ticker, 'en')
  #get nyt query and store as json
  nyt_json = nyt.autoQuery(ticker)

  formated_json = { 
            'articles': org_json['articles'] + nyt_json['articles']
  }
  return(formated_json)
