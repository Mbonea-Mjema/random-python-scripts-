from bs4 import BeautifulSoup as Html_parser
from requests import Session as Browser

#variables used
Documents={}# contains the contents of a particular course

"""
Document={course1:
          [list of links of assingments to course1],
          course2:
          [list of links of assingments to course2]}
"""
Newsforum=[]
course_name=[]
login_page="http://sulms.sharda.ac.in/login/index.php"


print("""
<<<<<<<<<<<<<WELCOME TO SHARDA LMS>>>>>>>>>>
      """)

#Getting credentials
username=input("Enter your username ")
password=input("Enter your password  ")

login_credentials={
             "username":username,
             "password":password
                    } #contains the username and password

with Browser() as Browser_tab:
    # posting login credentials in the login page
    #On succesful login
    dashboard_raw=Browser_tab.post(login_page,data=login_credentials)
    print("Signed in....")

    #parsing the raw html 
    dashboard=Html_parser(dashboard_raw.text,"html.parser")

    print("finding your courses...")
    #Finding course newsfeed links and course names
    
    for course in dashboard.findAll("div",{"class":"box coursebox"}):
        course_name.append(course('a')[0].attrs["title"].split("_")[0])
        Newsforum.append(course('a')[0].attrs["href"])

    print("Found all courses...")

    print('Collecting assignments...')
    for link in Newsforum:
        #Progress (in percentage)
        percentage=int((Newsforum.index(link)+1)/len(Newsforum)*100)

        print(str(percentage)+'%...')
        #going to the newsforum page
        Newsforum_html=Browser_tab.get(link)

        #parsing the html 
        Newsforum_page=Html_parser(Newsforum_html.text,"html.parser")


        #finding the main assignment page link
        Assignment_link=Newsforum_page.find("div",{"class":"activityinstance"})('a')[0].attrs['href']
        
        #opening the assignment page

        Assignment_page_raw=Browser_tab.get(Assignment_link)

        Assignment_page=Html_parser(Assignment_page_raw.text,'html.parser')
        
        
        File_links=[]
        for link1 in Assignment_page.findAll('td',{'class':"topic starter"}):
            if link1 != None:
                File_links.append(link1('a')[0].attrs['href'])
                
                
        if(File_links!=[]):
            assignment_links=[]
            for link2 in File_links:
                file=Browser_tab.get(link2)
                if(Html_parser(file.text,"html.parser").findAll("div",{"class":"attachments"})!= []):
                        #creating a link to the documents
                    name=Html_parser(file.text,"html.parser").findAll("div",{"class":"attachments"})[0]("a")[1].text
                    file=Html_parser(file.text,"html.parser").findAll("div",{"class":"attachments"})[0]("a")[0]
                    
                    #assignment_links.append(file.attrs["href"])
                    assignment_links.append((file.attrs["href"],name))

            Documents[course_name[Newsforum.index(link)]]=assignment_links               

        else:
            Documents[course_name[Newsforum.index(link)]]=[]

    print("Done with Doucuments")
    print("downloading files..")

        #downloading and creating files
    keys=list(Documents.keys())
    for key in Documents:
        #Progress (in percentage)
        
        percentage=int((keys.index(key)/len(keys)*100))
        print(str(percentage)+'%...')
        if Documents[key]!=[]:
            folder="./files/"+key.lower()
            import os
            if not os.path.exists(folder):
                os.makedirs(folder)
            for element in Documents[key]:
                link,name=element
                file_name = folder+"/"+name
                r = Browser_tab.get(link, stream=True)
                if not os.path.exists(file_name):
                    with open(file_name, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024): 
                            if chunk: # filter out keep-alive new chunks
                                f.write(chunk)
    
                                    
    print("done!!!!")

import shutil,os
files=os.listdir('./files')
for file in files:
	print('{}: {}'.format(files.index(file),file))
index =int(input('choose:...'))
folder=files[index]
shutil.make_archive('zippy', 'zip', './files/'+folder)
    
   
    
