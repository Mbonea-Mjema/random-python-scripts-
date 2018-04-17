'''
Project Name :Sharda university vattendance
Project by   : Mbonea Mjema
Year         :2017
'''
from requests import Session as Search
from bs4 import BeautifulSoup as bs
import re


def attendance(credentials):
    login_url="http://sharda.vattendance.in/"
    pattern=re.compile(r'\wat (\d\d\d\d\d\d\d\d\d) (.*)')
    details=pattern.findall(credentials)
    roll_number=details[0][0]
    print(roll_number)
    password=details[0][1]
    print(password)
    data={"username":roll_number,
          "password":password,
          "submit":"login"}

    with Search() as s:
        
            dash_board=s.post("http://sharda.vattendance.in/",data=data)
            print("verifying credentials....")
            assert len(dash_board.text)>10000,"invalid credentials"
            print("logged in....")
            html=s.get("http://sharda.vattendance.in/stu_complete_report")

    attendance=bs(html.text,"html.parser").find("tfoot" )
    name=bs(html.text,"html.parser").find("span",{"class":"username username-hide-on-mobile"})
    
    percentage=attendance('th')[4].text

    return percentage,name.text
