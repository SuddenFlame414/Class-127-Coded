from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Edge()
browser.get(start_url)
time.sleep(10)

planets_data = []

def scrape():
    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else :
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by = By.XPATH,value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()

scrape()
headers = ["Name","Light_Years_from_Earth", "Planet_Mass", "Stellar_Magnitude", "Discovery_Date"]
planet_df = pd.DataFrame(planets_data, columns=headers)
planet_df.to_csv("Planets.csv", index = True, index_label = "ID")