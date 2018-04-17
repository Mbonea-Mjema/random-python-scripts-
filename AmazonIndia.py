'''
AMAZON INDIA SCRAPER

BY MBONEA MJEMA
  2017

modules used:
    1.BeautifulSoup4
    2.re  (Regular Expressions)
    3.urllib

NOTE!!!!!!!!!
some products do not have prices this can create a mix
 '''

import re
from urllib.request import urlopen as up
from urllib.request import Request as req
from bs4 import BeautifulSoup as bs


header={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }

#loop variable
choice=""

#initialize the program
def init():
    user=input("Enter your search item ")
    user=user.replace(" ","+")
    url="http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+user
    s=req(url,data=None,headers=header)
    html=up(s)
    return html


def PrintData(name,price):
    for i in range(len(name)):
        print("Product Name = "  +name[i])
        print("Price = "+ price[i])
        print()
        print()



print("+++++++++++++++++++++Welcome to AMAZON INDIA+++++++++++++++++++++++++++++++++++++++")
while choice != "n":
  
     #get html code
    try:
        code=init()

    except Exception as e:
        print("ERROR !!!!")
        print("Check your Internet connection")
        break
    html=code

    #created soup object
    soup=bs(html.read(),"html.parser")

    #Roughly find the prices from soup object
    Raw_prices=soup.find_all("span",{"class":"a-size-base a-color-price s-price a-text-bold"})

    #Roughly find the names from soup object
    Raw_names=soup.findAll("h2",{"data-attribute":True})

    #create a product name pattern
    name_pattern=re.compile(r'\ data-attribute="(.*?)" ')

    #create a product price pattern
    price_pattern=re.compile(r'\</span>(.*?)</span>')

    #create a list of product names
    List_of_names=name_pattern.findall(str(Raw_names))

    #create a list of product prices
    List_of_prices=price_pattern.findall(str(Raw_prices))


    #print results
    try:
        PrintData(List_of_names,List_of_prices)

    except Exception as err:
        print("Some products dont have prices ")

    #for the loop 
    choice=input("Continue(y/n)?   ")



