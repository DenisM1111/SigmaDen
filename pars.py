import time
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service('C:/ch/chromedriver.exe')
browser=webdriver.Chrome(service=s)
browser.get("https://www.kinopoisk.ru/lists/movies/top250/")
time.sleep(10)
html_text=browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
df=soup.find('div',class_='base-movie-main-info_mainInfo__ZL_u3')
print(df)
alt=soup.find('span',class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
print(alt)