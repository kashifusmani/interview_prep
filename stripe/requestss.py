from requests import get, post
from json import loads

def test_requests():


    with open('data.txt') as f:
        for entry in f:
            payload = loads(entry, strict=False)
            print(payload)
    #post('https://httpbin.org/post', data=payload)

if __name__ == '__main__':
    test_requests()