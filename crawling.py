import re
import requests
from bs4 import BeautifulSoup

def getImage(keyword,no):
    url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
    html = requests.get(url)
    bs_html = BeautifulSoup(html.content,"html.parser")
    photowall = bs_html.find('div',{"class":"photowall"})
    img_list = photowall.find_all("img",{"class":"_img"})

    # for i in range(len(img_list)):
    for i in range(no):
        img_link = re.findall('data-source="(.+?)"',str(img_list[i]))[0]
        img_con = requests.get(img_link).content
        file = open("num1/"+keyword+str(i+1)+".jpg","wb")
        file.write(img_con)
        file.close()
        print(img_link)


getImage('점자 ',100)