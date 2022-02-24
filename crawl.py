from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_binary 
import os
import selenium
import pandas as pd
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from datetime import datetime, timedelta



class execute():
    def __init__(self,url,elements,settings):
        self.url = url
        self.elements = elements
        
        self.Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
        self.date = self.Previous_Date.strftime('%Y-%m-%d')
        self.day = self.Previous_Date.day

        self.settings = settings

        self.options = Options()
        self.options.headless = False
        self.options.add_argument("--window-size=1920,1200")
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=self.options)
        self.driver.get(self.url)
        time.sleep(3)
        
        try:
            # Click on date picker
            self.driver.find_element_by_xpath("//input[@class='datepicker hasDatepicker']").click()
            time.sleep(3)

            # Click on previous day
            self.driver.find_element_by_xpath("//a[text()="+str(self.day)+"]").click()
            time.sleep(3)
            
            # Submit date
            self.driver.find_element_by_xpath('//input[@type="submit"]').click()
            time.sleep(5)

        except:
            pass
        time.sleep(3)


    def crawler(self):

        # Return basic element      
        self.elem = self.driver.find_elements_by_xpath(self.elements)
        
        # Save data in an array
        data = [[row.find_element_by_xpath(self.settings[i]).text for i in self.settings] for row in self.elem]

        # Convert array to Dataframe
        crawled_data = pd.DataFrame(data, columns=[*self.settings])
        
        # Save data to csv file
        crawled_data.to_csv('C:\\Users\\User\\OneDrive\\Desktop\\Apiron\\Crawler\\infobeto.csv', index=False, encoding="utf-8-sig")
       
        # Close driver
        self.driver.close()





settings = {
    'Δ':".//td[@class='flag']",
    'ΩΕ': ".//td[@class='gameHour']",
    'Α': ".//td[3]",
    '1' : ".//td[3]",
    'ΓΗΠΕΔΟΥΧΟΣ' : ".//td[@class='team1']",
    'Χ' : ".//td[8]",
    'ΦΙΛΟ/ΝΟΥΜΕΝΗ' : ".//td[@class='team2']",
    '2' : ".//td[10]",
    '1Χ':".//td[11]",
    '12' : ".//td[12]",
    'Χ2': ".//td[13]",
    'Under' : ".//td[14]",
    'Over' : ".//td[15]",
    'Goal' : ".//td[16]",
    'No Goal': ".//td[17]",
    'Ημ/νο': ".//td[18]",
    'Τελικο':".//td[19]",
    'Σημ.' : ".//td[20]",
    'Αποδ' : ".//td[21]"


}

#exec = execute('https://www.infobeto.com/kouponi-opap',"//div[@class='table-responsive']//tbody/tr[@class='lineHeight']",settings)
#exec.crawler()
print(1-timedelta(1))


