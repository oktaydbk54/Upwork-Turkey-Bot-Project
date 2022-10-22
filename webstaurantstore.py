import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

import requests as re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




def collect_each_item_link(link):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    
    driver.get(link)
    time.sleep(3)
    elems = driver.find_element(By.ID,value = 'product_listing')
    
    all_links = list()
    
    a = elems.find_elements(By.TAG_NAME,value='a')
    
    for elem in a:
        href = elem.get_attribute('href')
        if href is not None and 'plus' not in href:
            all_links.append(href)
    
    
    all_link_set = set(all_links)
    new_all_links = list(all_link_set)

    print("finish")
    return new_all_links


def collect_information_item(links):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    print("Start")
    
    driver.get(links)
    time.sleep(2)
    
    price,product_name,description = None,None,None
    
    try:
        product_name = driver.find_element(By.XPATH,value = '//*[@id="page-header-description"]').text
    except:
        pass
    
    try:
        price = driver.find_element(By.XPATH,value = '//*[@id="priceBox"]/div[2]/div/p[1]').text    
    except:
        pass
    
    try:
        description = driver.find_element(By.XPATH,value = '//*[@id="details-group"]').text
    except:
        pass
    
    values = {'Product Name: ':product_name,
              'Price: ':price,
              'Description: ':description}
    
    return values


    

if __name__ == '__main__':
    
    link = "https://www.webstaurantstore.com/13393/countertop-glass-door-refrigerators-and-freezers.html"
    
    run_2 = collect_each_item_link(link)
    all_info = list()    
    for item in run_2[:10]:

        run_3 = collect_information_item(item)

        all_info.append(run_3)

    df = pd.DataFrame(all_info)
    
    df.to_excel('results.xlsx',index=False)















