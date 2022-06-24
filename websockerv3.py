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
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
    time.sleep(15)
    chrome.switch_to.default_content()
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/bframe?hl=en&v=M10Y1otwqRkBioiFUKRQ8s3N&k=6LfDlbAbAAAAALJvKffc-P-uv5EVxTN9gdyO1O4x']")))
    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='solver-button']"))).click() 
    print("Tıkladım v2")
    time.sleep(500)
    #//*[@id="solver-button"]  /html/body/div[7]/div[4]/iframe


bros()
