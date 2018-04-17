from bs4 import BeautifulSoup as bs 
from requests import Session as Search


def documents():
    Documents={}
    #login url
    url="http://sulms.sharda.ac.in/login/index.php"

    #user input
    print("##########_______SHARDA UNIVERSITY  LMS LOGIN_________########## ")
    user=input("Enter username ")
    password=input("Enter the password ")

    #user_data
    data={
    "username":user,    
    "password":password
    }
    
    #opening request object
    with Search() as s:
        #posting user infomation in the login page
        dashboard=s.post(url,data=data)
        print("signed in...")

        #creating course link list
        print("creating a course list")
        course_links=[course('a')[0].attrs["href"] for course in bs(dashboard.text,"html.parser").findAll("div",{"class":"box coursebox"})]
        course_name=[course('a')[0].attrs["title"].split("_")[0] for course in bs(dashboard.text,"html.parser").findAll("div",{"class":"box coursebox"})]
        print("opening course links and running mega loop")

        
        for directory in course_links:
            #opening the course links
            data = s.get(directory)

            #list of assignment_paths of a given subject
            assingment_path=[link('a')[0].attrs['href'] for link in bs(data.text,"html.parser").findAll("div",{"class":"activityinstance"})]

            #moving up the directory
            tuit=s.get(assingment_path[0])

            #assignment path
            
            
            path=[link('a')[0].attrs['href'] for link in bs(tuit.text,"html.parser").findAll('td',{'class':"topic starter"}) if bs(tuit.text,"html.parser").findAll('td',{'class':"topic starter"})!=[] ]
            if(path!=[]):
                assignment_links=[]
                for link in path:
                    file=s.get(link)
                    if(bs(file.text,"html.parser").findAll("div",{"class":"attachments"})!= []):
                        #creating a link to the documents 
                        assignment_links.append(bs(file.text,"html.parser").findAll("div",{"class":"attachments"})[0]("a")[0].attrs["href"])
                Documents[course_name[course_links.index(directory)]]=assignment_links               

            else:
                Documents[course_name[course_links.index(directory)]]=[]
                        
                   
                
        print("downloading files..")

        #downloading and creating files
        for key in Documents:
            if Documents[key]!=[]:
                folder="./files/"+key
                import os
                if not os.path.exists(folder):
                    os.makedirs(folder)
                for link in Documents[key]:
                    file_name = folder+"/"+link.split('/')[-1].replace("%20"," ")
                    r = s.get(link, stream=True)
                    if not os.path.exists(file_name):
                        with open(file_name, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=1024): 
                                if chunk: # filter out keep-alive new chunks
                                    f.write(chunk)
                                    
        print("done!!!!")
        return(Documents)

data=documents()        
        
