import requests

session = requests.Session()

def get_countries(country_str):
    URL = "https://jsonmock.hackerrank.com/api/countries/search"

    params = {
        "name": country_str,
    }

    results = session.get(URL, params=params).json()
    yield results

    num_pages = results['total_pages']
    for page in range(2, num_pages + 1):
        params["page"] = page
        next_page = session.get(URL, params=params).json()
        yield next_page


def get_countries_with_population_over_num(countries, num):
    count = 0

    for country in countries:
        if country["population"] > num:
            count+=1

    return count

def getCountries(country_str, population):

    count = 0
    for countries in get_countries(country_str=country_str):
        count += get_countries_with_population_over_num(countries=countries["data"], num=population)

    return count

if __name__ == '__main__':
    print(getCountries('un', 100090))