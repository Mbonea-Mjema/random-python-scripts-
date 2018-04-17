'''
project: Bible verses
website: biblestudytools.com
written by: Mbonea Mjema
year: 2017

Libraries used:
    pprint(PrettyPrinter)
    beautifulsoup
    requests
'''


import pprint
from bs4 import BeautifulSoup as bs
from requests import Session as Search

#here are the topics for the bible verses
topic=["love","peace","friendship","encouraging","forgiveness","strength","inspirational","hope",'bible-verses-for-times-of-adversity']

#print topic options
for t in topic:
    print(str(topic.index(t)+1)+" :",t)

#user input
choice=input("Enter your choice  ")
assert type (int(choice)) is int and 1 <= int(choice) <= 9, "invalid input"
choice=int(choice)-1

#url
if not '-' in topic[choice]:
    url="http://www.biblestudytools.com/topical-verses/"+topic[choice]+"-bible-verses/"
else:
    url="https://www.biblestudytools.com/topical-verses/"+topic[choice]+"/"

#making the web request
raw_html=Search().get(url)

#parsing with BeautifulSoup
Soup_object=bs(raw_html.text,"html.parser")

#image from the request
image=Soup_object.findAll("meta",{"property":"og:image"})[0].attrs["content"]

#verses and heading
verses=Soup_object.findAll("div", {"class":"scripture"})
heading=Soup_object.findAll("h2",{"class":"list-group-item-heading"})

#organise
Word={heading[index_].text:verses[index_].text for index_ in range(len(verses))}

#printting
pp=pprint.PrettyPrinter ()
pp.pprint(Word)

print(image)
