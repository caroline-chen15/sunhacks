#https://towardsdatascience.com/how-to-scrape-any-website-with-python-and-beautiful-soup-bc84e95a3483
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag

import requests
from bs4 import BeautifulSoup
import geopy
from geopy.geocoders import Nominatim

URL = 'https://devpost.com/hackathons?utf8=%E2%9C%93&search=&challenge_type=in-person&sort_by=Recently+Added'
page = requests.get(URL)
#txt = page.text

src = page.content
soup = BeautifulSoup(src, features="html.parser")
titles = soup.find_all('h2', attrs={'class':'title'})
places = soup.find_all('p', attrs={'class':'challenge-location'})
hacks = []
locations = []
for i in titles:
    hacks.append(i.string[17:-15])
for i in places:
    str_pl = str(i)
    spliced = str_pl[69:-21]
    locations.append(spliced)

locator = Nominatim(user_agent="myGeocoder")
masterlist = []
for i in locations:
    listy = []
    location = locator.geocode(i)
    listy.append(i)
    listy.append(location.longitude)
    listy.append(location.latitude)
    masterlist.append(listy)

return masterlist