# Aditya Subramanian Muralidaran

'''
1. Enter the actual apiKey.
2. Run in batch to conditions of API hit per day and per minute.
'''

import urllib.request
import urllib.response
import json
from bs4 import BeautifulSoup
import requests


apiKey = '5419e042517b490094580b2e38865bc9'

searchTerm = 'attack'
#searchTerm = 'shooting'
#searchTerm = 'gun'

writeFile = open("NYT_Content_Attack.txt", "a", encoding='utf-8')
for i in range(11):
    print(i)
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='+searchTerm+'&begin_date=20180330&end_date=' \
        '20180405&page='+str(i)+'&fl=web_url&api-key='+apiKey
    response = urllib.request.urlopen(url)
    if (response.getcode() == 200):
        data = json.load(response)
        for doc in data['response']['docs']:
            print(doc['web_url'])
            html_code = requests.get(doc['web_url'])
            plain_text = html_code.text
            soup = BeautifulSoup(plain_text,'html.parser')
            for para in soup.find_all('p',{'class':'story-content'}):
                writeFile.write(para.get_text())
                writeFile.write("\n")

writeFile.close()

