'''
joel osteen 31 daily declarations

'''


from requests import Session as browser
from bs4 import BeautifulSoup as parser
tab=browser()
response=tab.get('https://jacquelineswow.com/2013/11/10/31-declarations-to-speak-over-your-life/')
data=parser(response.content,'lxml')
info=data.find('div' ,{'class':"entry-content"}).text.split('\n')

'starts at info[2]to info[32]'
