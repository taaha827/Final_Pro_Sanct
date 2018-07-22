#This Code is used to scrap images from different websites depending on their structure
#Developed by Prosanct
#Develped Date: 7/5/2018
#Modified Date: 7/5/2018

try:
    import sys
    sys.path.append('C:\\wamp64\\www\\ProSanct-Web-Scrapper-master')
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import re
    import requests
    import glob


    #importing the necessary libraries
    from PIL import Image
    #This library will help us read the addresses of the files
    import glob
    #this is the external database class that we have created our selves
    import database
    #this library will process the images and will extract data from them
    import pytesseract
    import datetime
    #this is a neccessaty as it is used to set the run time enviroment variable in windows this address should be where you have downloaded and extracted the tesseract.exe file you can find that by a single google search
    import sys
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\tesseract-ocr\\tesseract.exe'

    class scraping:
        jpgs = None
        pngs = None
        mergedLists = None
        url = None
        browser= None
        html = None
        soup = None
        img = None
        imgs =None
        Callee=None
        FileNames =[]
        city=None
        category=None
        db = database.Database()
        bannertype = ""
        textread= ""
        def __init__(self):
            self.url="http://pixabay.com"
            print(self.url+"Default Constructor is called")
        def __init__(self,data,calee,city,category):
            #This is where the link of the website goes which we want to scrap
            self.url=data
            self.Callee=calee
            self.city=city
            self.category=category
            query = "Select FilePath From daraz_data WHERE Website ='"+self.url+"'"
            aa=self.db.query(query)
            for x in aa:
                xa = x['FilePath']
                self.FileNames.append(xa)
 

        def getresponse(self):
            #We use PhantomJS because we want the fully loaded page, not the response that is given by the browser in which the scripts have not run
            self.browser = webdriver.PhantomJS("C:\\wamp64\\www\\ProSanct-Web-Scrapper-master\\phantomjs")
            self.browser.get(self.url)


        #this is to get that specific webpage
        def extractresponse(self):
            #extracting the elements of the returned web page
            self.html = self.browser.page_source
            self.soup = BeautifulSoup(self.html, 'html.parser')


        def saving_image(self):
            if self.imgs ==[]:
                query = "INSERT INTO warnings (`SentBy`,`Warning`) VALUES('"+self.Callee+"','No Images have returned,Check the specific tags of "+self.Callee+")"
                self.db.insert(query)
            else:
                urls = [img['src'] for img in self.imgs]
                for url in urls:
                    if '?' in url:
                        u = url.split('?')
                        url = u[0]
                    
                    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
                    if filename is None:
                        print("Data is none")
                    else:
                        with open("C://wamp64/www/ProSanct-Web-Scrapper-master/"+self.Callee+"\\"+filename.group(1), 'wb') as f:
                    #if 'http' not in url:
                    # sometimes an image source can be relative
                    # if it is provide the base url which also happens
                    # to be the site variable atm.
                    # url = '{}{}'.format(site, url)
                    #getting the image at the mentioned source
                            if 'http:' in url or 'https:':
                                url = url
                            else:
                                u= "http:"
                                u =u+url
                                url=u
                            response = requests.get(url)

                        #Saving it in the directory where the script is running
                            f.write(response.content)

        def FilePathReader(self,folder_name):
        #readding all the addresses of the images that we have stored in .jpg format
            self.jpgs = glob.glob("C://wamp64/www/ProSanct-Web-Scrapper-master/"+folder_name+"\\*.jpg")

        #readding all the addresses of the images that we have stored in .png format
            self.pngs = glob.glob("C:/wamp64/www/ProSanct-Web-Scrapper-master/"+folder_name+"\\*.png")
            self.mergedLists= self.jpgs + self.pngs

        def specificextraction(self,tag,attribute,value):
            slider_div = self.soup.find_all(tag,{attribute:value})
            soup1 = BeautifulSoup(str(slider_div), "html.parser")
            self.imgs = soup1.find_all('img')

            #obj.datainsertion()



        """def findpercentage(self,text):
            stop = ""
            discount =""
            i=1
            for i in range (1,text.__len__()):

                if text[i] == '1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9':
                    discount+=text[i]
                if text[i] =='%':
                    stop=text[i]
                    break
            discount=discount+stop
        """
        def checksaleword(self):
            for words in ['sale', 'upto', 'off', 'up', 'to', 'flat']:
                if re.search(r'\b' + words + r'\b', self.textread.lower()):
                    return True
            return False

            """if(self.textread==""):
                return False
            print("TextRead"+self.textread)
            if(self.textread.find('sale')!=-1):
                print('sale')
                
                return True
            elif (self.textread.find('SALE')!=-1):
                print('SALE')
                return True
            elif (self.textread.find('off')!=1):
                print('off')
                return True
            elif (self.textread.find('upto')!=1):
                print('upto')
                return True
            elif (self.textread.find('up')!=1):
                print('up')
                return True
            elif (self.textread.find('to')!=1):
                print('to')
                return True
            elif (self.textread.find('flat')!=1):
                print('flat')
                return True
            """ 
              
                
        def checkaccuracy(self):
            for path in self.mergedLists:
                splitArr = path.split('\\')
                self.textread = pytesseract.image_to_string(Image.open(str(path)))
                print("Text Read:"+self.textread+"\n")
        def checkifexists(self,filename):
            for fi in self.FileNames:
                if filename == fi:
                    return 1
            return 0

        def datainsertion(self):
            a=0
            for path in self.mergedLists:
                t = self.Callee.split('\"')
                splitArr = path.split('\\')
                self.textread = pytesseract.image_to_string(Image.open(str(path)))
                if(self.checksaleword()):
                    self.bannertype='sales'
                else:
                    self.bannertype='nosale'
                #self.findpercentage(self.textread)
                if (self.checkifexists(path) == 1):
                    print("value")
                else:
                    query = "INSERT INTO daraz_data(`FilePath`,`TextRead`,`Website`,`City`,`URL`,`Category`,`PercentageOff`,`SalesType`,`address`,`brandname`,`BannerType`) VALUES("+ "'" +self.db.connection.escape_string(path) + "','" + self.db.connection.escape_string(self.textread) + "','"+self.url+"',"+"'"+self.city+"','"+self.url+"','"+self.category+"','"+str(30)+"','"+" "+"','localhost/ProSanct-Web-Scrapper-master/"+str(t[1])+"/"+splitArr[1]+"','"+self.Callee+"','"+self.bannertype+"')"
                    self.db.insert(query)
                    if(self.textread==""):
                        query="INSERT INTO warnings(`SentBy`,`Warning`) VALUES ('"+self.Callee+"','Image with name"+splitArr[1]+"reads empty string so check the image manually')"
                        self.db.insert(query)
except:
    print("There is an error occuring")
