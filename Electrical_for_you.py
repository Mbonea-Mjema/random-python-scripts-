from bs4 import BeautifulSoup as bs
from requests import Session as Search
while True:
    query=input('Enter a topic')
    query=query.replace(' ','-')
    url="https://electronicspost.com/"+query+"/"
    raw_html=Search().get(url)

    soup_obj=bs(raw_html.text,"html.parser")


    paragraphs=soup_obj.findAll("p",{"style":"text-align: justify;"})

    for paragraph in paragraphs:
        print(paragraph.text)
