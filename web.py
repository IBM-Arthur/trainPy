import bs4
import requests
from selenium import webdriver

res = requests.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=ibm')
res.encoding = 'UTF-8'

bs = bs4.BeautifulSoup(res.text,'html.parser')

elems = bs.select('.t a')

elems[0]['href']
