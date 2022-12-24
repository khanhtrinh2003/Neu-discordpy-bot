import requests
from bs4 import BeautifulSoup
import numpy as np

def news(x, nums):
    if x == 'NEU':
        # NEU
        neu_request = requests.get("https://daihocchinhquy.neu.edu.vn/")
        neu = BeautifulSoup(neu_request.content, "html.parser")
        news = neu.findAll('a', style='text-decoration:none')
        li=[]
        for new in news[:nums]:
            tit = new.text
            a = new.attrs["href"]
            link = 'https://daihocchinhquy.neu.edu.vn/'+a
            li.append([tit, link])
        return np.array(li).reshape(-1,1)

    elif x == "Economics":
        cafebiz_request = requests.get("https://cafebiz.vn/vi-mo.chn")
        cafebiz = BeautifulSoup(cafebiz_request.content, "html.parser")
        news = cafebiz.findAll('div', class_='cfbiznews_box')
        
        li=[]
        for new in news[:nums]:
            tit = new.find('a').attrs["title"]
            a = new.find('a').attrs["href"]
            link = 'https://cafebiz.vn'+a
            li.append([tit, link])
        return np.array(li).reshape(-1,1)   

 
