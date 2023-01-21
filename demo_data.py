import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [

    # 'https://www.abilityone.com/clc-controlled-life-cycle-plastic-bags/product/312510',
    'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010',


]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver",)
    driver.get(url)
    time.sleep(5)
    # # =================================================== Find Breadcrumb =================================================
    # print("********************************* Breadcrumb : ***********************************")
    # Breadcrumb = driver.find_element(By.XPATH, '//*[@id="breadcrumbs"]/div/div/div')
    # Breadcrumb_d = Breadcrumb.text.replace("\n", " ")
    # print("Breadcrumb = ", Breadcrumb_d)
    # #
    # # # =================================================== Find Title =================================================
    # print("*********************************** title : **************************************")
    # title = driver.find_element(By.CLASS_NAME, 'pdp_prodInfo-title')
    # title_d = title.text
    # print("Title = ", title_d)

    sku1 = driver.find_elements(By.TAG_NAME, "option")
    # for g in sku1:
    #     print(g.text)
    count = 0
    for x in sku1:
        count += 1
        x.click()
        time.sleep(5)
        # print(x.text)

        j = 1
        ta = x.find_elements(By.XPATH, '//*[@id="headingThree"]/h4/button')
        print(ta)
        for z in ta:
            j += 1
            print(j)
            time.sleep(3)
            z.send_keys('\n')
            spec = x.find_element(By.XPATH, '//*[@id="collapseThree"]')
            time.sleep(3)
            attr_name = spec.text
            print(attr_name.split(":")[-1:])

        # # =================================================== Find price =================================================
        # print("*********************************** Price : **************************************")
        # price = driver.find_element(By.XPATH, '//*[@id="pdp_prodInfo"]/p[2]')
        # print(count)
        # print("Selected option", x.text)
        # print("price", price.text)
        # # # =================================================== Find item number =================================================
        # print("*********************************** Item N : **************************************")
        # item = driver.find_elements(By.XPATH, '//*[@id="pdp_prodInfo"]/div/p[1]/span')
        # for item_n in item:
        #     item_d = item_n.text
        #     print('item_d = ', item_d)
        # # # =================================================== Find images =================================================
        # print("*********************************** Images : **************************************")
        # image = driver.find_element(By.XPATH, '//*[@id="main-slider-desktop"]/div[2]/div').find_elements(By.TAG_NAME, 'img')
        # for x in image:
        #     time.sleep(1)
        #     image_d = (x.get_attribute('src'))
        #     print("image_d = ", image_d)
        # # =================================================== Find Description =================================================
        # print("*********************************** Descriptions : **************************************")
        # description = driver.find_element(By.CLASS_NAME, 'panel-body').find_elements(By.TAG_NAME, 'p')
        # for zz in description:
        #     time.sleep(3)
        #     print("description = ", zz.text)

        # button = driver.find_element(By.TAG_NAME, 'button')
        # button.click()
        # print(button)
        # //*[@id="collapseThree"]/div/div/div[1]/ul'





