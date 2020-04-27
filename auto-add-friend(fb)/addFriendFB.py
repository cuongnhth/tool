import requests
from bs4 import BeautifulSoup
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
def initDriver(filePath):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir="+filePath)
    driver = webdriver.Chrome(
        'C:\chromedriver\chromedriver.exe', options=chrome_options)
    return driver


def ham_surf_face(filePath):
    driver = initDriver(filePath)
    driver.get('https://www.facebook.com')
    #time.sleep(2)
    #while(True):
        #time.sleep(2)
    # js = "document.querySelector('#findFriendsNav').click()"
    # driver.execute_script(js)
    a = driver.find_element_by_id('findFriendsNav')
    a.click()
    time.sleep(2)
    #btn_add_friend = driver.find_elements_by_css_selector('.FriendButton')
    #btn_add_friend = driver.find_element_by_link_text("Trang chủ")
    

    a = driver.find_element(By.XPATH, '//button[text()="Thêm bạn bè"]')
    time.sleep(2)
    a.click()
    time.sleep(2)
    #list_friend = len(btn_add_friend)
    #print(a)
    # print("start")
    # for i in list_friend:
    #     friend = i.find("button", class_="_42ft _4jy0 _4jy3 _4jy1 selected _51sy")
    #     friend.click()
    #     print("click: ", num)
    #     num+=1
    #     time.sleep(1)
    # print("end")


filePath = 'Nick_a'
ham_surf_face(filePath)
