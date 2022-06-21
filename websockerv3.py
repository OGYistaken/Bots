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




def get_proxy() :
    url = "https://free-proxy-list.net/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

print(get_proxy())


def bros() :
    options = webdriver.ChromeOptions()
    options.add_extension('extension_1_6_7_0.crx')
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.get("https://watcher.guru/coin/sportoken")
   
    chrome.execute_script("window.open('https://watcher.guru/coin/sportoken');")
    print("yolladım")
    time.sleep(20)


bros()
