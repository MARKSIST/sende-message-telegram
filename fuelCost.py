# scrape info from auto.ria.com
from bs4 import BeautifulSoup
import urllib.request as urllib2


def fuelCost(typeOfFuel=None):
    page = urllib2.urlopen('https://auto.ria.com/uk/toplivo/')
    soup = BeautifulSoup(page, 'html.parser')
    dataPrice = soup.findAll('div', attrs={'class': 't-cell bold size18'})
    dataName = soup.findAll('a', attrs={'class': 'i-block unlink-avg'})
    info = {}
    for names in dataName:
        for prices in dataPrice:
            info[names.text.strip(' A-')] = prices.text
            dataPrice.remove(prices)
            break
    if typeOfFuel is None:
        return info
    if info[typeOfFuel] == '-':
        text = 'Інформація відсутня. Спробуйте пізніше'
        return text
    return info[typeOfFuel]
