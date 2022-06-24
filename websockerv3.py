from socket import timeout
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
from random import choice
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_proxy() :
    url = "https://free-proxy-list.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

print(get_proxy())


def bros() :
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_extension('extension_1_6_7_0.crx')
    options.add_extension('extension_1_3_1_0.crx')
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.get("https://watcher.guru/coin/sportoken")
    print("yolladım")
    print("Tıkladım")
    element = chrome.find_element(By.XPATH, '//*[@id="vote-button"]') 
    element.click();
    time.sleep(5)
    iframes = chrome.find_elements_by_tag_name("iframe")
    chrome.switch_to.frame(chrome.find_elements_by_tag_name("iframe")[2])
    check_box = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.ID ,"recaptcha-anchor")))
    check_box.click()
    time.sleep(15)
   # iframes = chrome.find_elements_by_tag_name("iframe")
    #chrome.switch_to.frame(chrome.find_elements_by_xpath("/html/body/div[6]/div[4]/iframe"))
    #capt_btn = WebDriverWait(chrome, 50).until(
     #          EC.element_to_be_clickable((By.XPATH ,'//button[@id="solver-button"]'))
    #)
    #capt_btn.click()
    print("Tıkladım v2")
    time.sleep(500)
    #//*[@id="solver-button"]  /html/body/div[7]/div[4]/iframe


bros()
