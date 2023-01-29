from select import select

import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [

    'https://www.packardonline.com/products/ebm9137/',
    'https://www.packardonline.com/products/25318901/',
]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    # opts = Options()
    # opts.headless = True
    # driver = webdriver.Chrome(r"C:\Users\PK\Downloads\chromedriver_win32/chromedriver", options=opts)
    # driver.get(url)
    # time.sleep(5)
    print("Products urls", url)
    print()
    print("************************** BreadCrumb ***********************************")
    lists = []
    sku = soup.find_all('div', {"class": "breadcrumbs"})
    for x in sku:
        lists.append(x.text.replace("\n", ' '))
    bread = lists
    print("Breadcrumb = ", bread)

    print("************************** Title ***********************************")
    title = soup.find("h1", {"class": "title titleProduct"})
    title_d = title.text
    print("title = ", title_d)

    print("************************** Item Number ***********************************")
    unic = soup.find("div", {"class": "itemSku"})
    unic_d = unic.text
    print("unic = ", unic_d)

# ========================= image with soup =============================
    print("************************** Image ***********************************")
    image = soup.find('ul', {"class": "altViews"}).find_all('img')
    for img in image:
        image_d = (img.get('src'))
        print("image = ", image_d)

# ========================= image with selenium =============================
#     image = driver.find_element(by=By.CLASS_NAME, value='altViews').find_elements(by=By.TAG_NAME,value='img')
#     for img in image:
#         image_d = (img.get_attribute('src'))
#         print("image = ", image_d)
    try:
        print("************************** Feature ***********************************")
        feature = soup.find("div", {"id": "product-tab-0"})
        feature_d = (feature.text.strip())
        print("feature", feature_d)
    except:
        feature_d = "Not Found"
        print(feature_d)

    try:
        print("**************************** pdf ***********************************")
        pdf = soup.find('a', {"class": "download-link"})
        pdf_d = pdf.get('href')
        print(pdf_d)
    except:
        pdf_d = "Not Found"
        print(pdf_d)

    #   ================================table ==================================
    table = soup.find("table", {"class": "table-responsive-simple"})
    attr_name = table.find_all('th')
    attr_value = table.find_all('td')
    for th in attr_name:
        attr_name_d = th.text
        print("attr_name", attr_name_d)
    for td in attr_value:
        attr_value_d = td.text
        print("attr_value", attr_value_d)

#    ==========================table2 ==================================
    table2 = soup.find("div", {"id": "product-tab-2"})
    attr_name1 = table2.find_all('th')
    attr_value1 = table2.find_all('td')
    for th in attr_name1:
        attr_name_d1 = th.text
        print("attr_name", attr_name_d1)
    for td in attr_value1:
        attr_value_d1 = td.text
        print("attr_value", attr_value_d1)













