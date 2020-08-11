import requests
from json import loads

url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=%s&page=%d'

def getMovieTitles(substr):
    cur_page = 1
    total_pages = 1
    titles= []
    while cur_page <= total_pages:
        resp = requests.get(url % (substr, cur_page))
        json_resp = loads(resp.content)
        total_pages = json_resp['total_pages']
        for item in json_resp['data']:
            titles.append(item['Title'])
        cur_page = cur_page + 1

    titles.sort()
    for item in titles:
        print(item)

if __name__ == '__main__':
    getMovieTitles('spiderman')