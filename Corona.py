import tweepy
import time
import requests
from bs4 import BeautifulSoup

CountryName = 'Sri Lanka'

def begin_dissection(res):
    global Tot
    global IPM
    Tot = res[12:15]
    # print(Tot)
    IPM = res[34:39]
    # print(IPM)

def get_corona():
    URL = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    # soup = BeautifulSoup(URL)
    countries = soup.find_all('tr')
    for country in countries:
        str = country.get_text()
        if CountryName in str:
            res = str
            # print(str)
            # print(len(str))
            begin_dissection(res)
    ReplyString = 'Sri Lanka\nNo. Of Covid-19 Patients: ' + Tot + '\nNo. Of Patients Per Million Of Population: ' + IPM
    print(ReplyString)
get_corona()