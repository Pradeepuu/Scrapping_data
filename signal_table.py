import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
mylist = [
    'https://signaling.fedsig.com/product/300fp-field-programmer/300FP-SD',
    'https://signaling.fedsig.com/product/cts2-amplifiers/CTS2-300N-120-240',
]
for url in mylist:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver")
    driver.get(url)
    time.sleep(6)

    print("************************************* table section 1 : ****************************************")
    attr_n = []
    attr_v = []
    table = driver.find_elements(By.XPATH, '//*[@id="FSProductSpecifications_v1-wi600001"]/div/div/div/section/table')
    # print(table.text)
    i = 0
    for x in table:

        # print(i)
        # print(x.text)
        td = x.find_elements(By.TAG_NAME, 'td')
        for g in td:
            i = i + 1
            if i % 2 == 0:
                attr_v.append(g.text)
            else:
                attr_n.append(g.text)
    # print(attr_n)
    # print(attr_v)
    for m, n in zip(attr_n, attr_v):
        print(m, " = Table Section 1 = ", n)

    print("************************************* Table Section 2 : ****************************************")
    lists = []
    lists1 = []
    table2 = driver.find_elements(By.ID, 'sku-specification-table')
    for th in table2:
        th1 = th.find_elements(By.TAG_NAME, 'th')
        for t in th1:
            lists.append(t.text)
        td1 = th.find_elements(By.TAG_NAME, 'td')
        for t in td1:
            lists1.append(t.text)
    for o, p in zip(lists, lists1):
        print(o, "= Table section 2 = ", p)

