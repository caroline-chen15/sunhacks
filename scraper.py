#https://towardsdatascience.com/how-to-scrape-any-website-with-python-and-beautiful-soup-bc84e95a3483
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag

import requests
from bs4 import BeautifulSoup
import geopy
from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='C:\\Users\\cc\\Documents\\GitHub\\sunhacks\\chromedriver_win32\\chromedriver.exe')
url = "https://devpost.com/hackathons?utf8=%E2%9C%93&search=&challenge_type=in-person&sort_by=Submission+Deadline"
driver.get(url)

while True:
    try:
        load = driver.find_element_by_link_text("Load more hackathons")
        time.sleep(2)
        load.click()
        time.sleep(2)
    except Exception as e:
        #print(e)
        break
#print("Complete")
time.sleep(2)
page_source = driver.page_source
driver.quit()

#URL = 'https://devpost.com/hackathons?utf8=%E2%9C%93&search=&challenge_type=in-person&sort_by=Recently+Added'
#page = requests.get(URL)
#txt = page.text
#src = page.content
soup = BeautifulSoup(page_source, features="html.parser")
titles = soup.find_all('h2', attrs={'class':'title'})
places = soup.find_all('p', attrs={'class':'challenge-location'})
#print(titles)
#print(places)
hacks = []
locations = []

def manip():
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
        if i == "":
            listy.append("")
        else:
            location = locator.geocode(i)
            listy.append(i)
            listy.append(location.longitude)
            listy.append(location.latitude)
        masterlist.append(listy)

    return hacks, masterlist