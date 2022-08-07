import requests
from bs4 import BeautifulSoup


def get_city():
    URL = "https://randomcity.net/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs={'class': 'text-center text-2xl font-bold text-purple-900'})
    list = []
    for row in table:
        list.append(str(row.text).strip().replace(",", ""))
    list.pop(0)
    return list
