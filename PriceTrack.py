from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
#List of websites:
l1=["https://www.amazon.in/dp/B09V4B6K53?th=1",'https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXQGX7PK&marketplace=FLIPKART&q=iphone+13++128&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=270ebfac-64f1-49bc-9f0d-1eef50efe185.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=73a1dlsq6o0000001676389263451&qH=98e4e25f9df2f53b','https://www.reliancedigital.in/apple-iphone-13-128-gb-starlight/p/491997700']
for i in l1:
    if(i==l1[0]):
        driver.get("https://www.amazon.in/dp/B09V4B6K53?th=1")
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('h1', class_='a-size-large a-spacing-none')
        product_prices = soup.find_all('span', class_='a-price-whole')
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)
    if(i==l1[1]):
        driver.get('https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXQGX7PK&marketplace=FLIPKART&q=iphone+13++128&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=270ebfac-64f1-49bc-9f0d-1eef50efe185.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=73a1dlsq6o0000001676389263451&qH=98e4e25f9df2f53b')
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('span', class_="B_NuCI")
        product_prices = soup.find_all('div', class_='_30jeq3 _16Jk6d')
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)
    if(i==l1[2]):
        driver.get('https://www.reliancedigital.in/apple-iphone-13-128-gb-starlight/p/491997700')
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('h1', class_='pdp__title mb__8')
        product_prices = soup.find_all('span', class_='pdp__offerPrice')
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)
