from requests import Session as Search
from bs4 import BeautifulSoup as bs

#Taking the  user image  request
def bing(user_request):
    
    user_request=user_request.replace(" ","+")
    url="https://www.bing.com/images/search?q="+user_request+"&FORM=HDRSC2"

    #Getting the raw html code
    raw_html=Search().get(url)

    #image list
    raw_images=[image.attrs["href"] for image in bs(raw_html.text,"html.parser").findAll("a",{"class":"thumb"})]

    return(raw_images)
