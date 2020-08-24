import requests
from bs4 import BeautifulSoup

URL = 'https://sinoptik.ua/погода-'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}

def get_html(url, params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='tabs')[0]
    day_of_week = items.find('p', class_='day-link').get_text()
    day = items.find('p', class_='date').get_text()
    month = items.find('p', class_='month').get_text()

    min = items.find('div', class_='min')
    min_temprature = min.find('span').get_text()
    max = items.find('div', class_='max')
    max_temprature = max.find('span').get_text()

    content = []
    content.extend([day_of_week, day, month, min_temprature, max_temprature])
    return content

def get_name_of_city(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find_all('div', class_='cityName cityNameShort')[0]
    name_of_city = name.find('strong').get_text()
    return name_of_city

def parse(city):
    html = get_html(URL + city)
    data = get_content(html.text)
    name_of_city = get_name_of_city(html.text)
    return  data, name_of_city
