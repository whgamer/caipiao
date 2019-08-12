import requests
from time import *
from random import randint
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
data =""
url =""
r =requests.post(url,data=data,headers =headers)