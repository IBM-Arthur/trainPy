import bs4
import requests
from selenium import webdriver

res = requests.get('http://baidu.com')
res.encoding = 'UTF-8'

bs = bs4.BeautifulSoup(res.text)

elems = bs.select('.t a')
