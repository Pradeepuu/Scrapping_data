import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [
    'https://www.abilityone.com/led-t8-tube-light/product/45055',
    # 'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010',
    #     'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010',
    #     'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-oil-only/product/64010',
    #     'https://www.abilityone.com/duck-sorb-reg-13-gallon-spill-kit-universal/product/64015',
    # 'https://www.abilityone.com/first-aid-kit-field/product/62025?recset=-3edf1204%3A185b886138b%3A18b2-20',

]
for url in Result:
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.prettify())
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", )
        driver.get(url)
        time.sleep(5)

        sku1 = driver.find_elements(By.TAG_NAME, "option")
        # for g in sku1:
        #     print(g.text)
        count = 0
        a = ""
        b = ""
        for x in sku1:
            count += 1
            x.click()
            time.sleep(5)
            # print(x.text)
            j = 1
            ta = x.find_elements(By.XPATH, '//*[@id="headingThree"]/h4/button')
            for z in ta:
                j += 1

                # time.sleep(3)
                z.send_keys('\n')
                spec = x.find_element(By.XPATH, '//*[@id="collapseThree"]')
                time.sleep(3)
                attr_name = spec.text
                attr_name1 = spec.text.split('\n')
                for xy in attr_name1:
                    attr_name_new = xy.split(':')
                    a = (attr_name_new[0])
                    b = (attr_name_new[1:])
                    print(a)
                    print(b)
                    save_details: TextIO = open("tablett.xlsx", "a+", encoding="utf-8")
                    save_details.write("\n" + a + "\t" + "".join(b))
                    print("End")
                    save_details.close()
                    print("\n ***** Record stored into Table Specifications . *****")
                    print()
    except Exception as e:
        print(e)

