from email import header
from lib2to3.pgen2 import driver
from random import randrange
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.common.by import By
START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrap():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index, li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element(By.XPATH, value='//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open("scrapper.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrap()    
