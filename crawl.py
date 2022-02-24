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
from datetime import datetime




class execute():
    def __init__(self,url,elements,settings,Date):
        self.url = url
        self.elements = elements

        self.date = Date['choose_date']
      
        self.months_dictionary = {'1':'Ιανουάριος','2':'Φεβρουάριος','3':'Μάρτιος','4':'Απρίλιος','5':'Μάιος','6':'Ιούνιος',
                                    '7':'Ιούλιος','8':'Αύγουστος','9':'Σεπτέμβριος'}
   
    
        self.settings = settings

        self.options = Options()
        self.options.headless = False
        self.options.add_argument("--window-size=1920,1200")
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=self.options)
        self.driver.get(self.url)
        time.sleep(3)

        if self.date=='False':     

            self.Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
            self.date = self.Previous_Date.strftime('%Y-%m-%d')
            self.day = self.Previous_Date.day

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
        else:

            
            self.month  = datetime.strptime(self.date,'%Y-%m-%d').month
            self.day  = datetime.strptime(self.date,'%Y-%m-%d').day

            try:
                # Click on date picker
                self.driver.find_element_by_xpath("//input[@class='datepicker hasDatepicker']").click()
                time.sleep(3)

                # Search month
                search_month = self.driver.find_element_by_xpath('//span[@class="ui-datepicker-month"]').text

                while search_month!=self.months_dictionary[str(self.month)]:

                    # Click button until the desired month is found
                    self.driver.find_element_by_xpath('//a[@class="ui-datepicker-prev ui-corner-all"]').click()
                    search_month = self.driver.find_element_by_xpath('//span[@class="ui-datepicker-month"]').text
                    time.sleep(2)
                
                # Click on correct day
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
        crawled_data.to_csv('C:\\Users\\Βίκη\\Desktop\\Επιφάνεια εργασίας_XP\\GAMES\\infobeto_'+str(self.date)+'_.csv', index=False, encoding="utf-8-sig")
       
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

# Date in form 2022-01-05
Date = {
    'choose_date':'2022-01-08'   # if executed on previous date assign 'False'
}

exec = execute('https://www.infobeto.com/kouponi-opap',"//div[@class='table-responsive']//tbody/tr[@class='lineHeight']",settings,Date)
exec.crawler()




