import sys

from bs4 import BeautifulSoup

sys.path.append('C:\\wamp64\\www\\ProSanct-Web-Scrapper-master')
import scrapping_image
import database
db =database.Database()

if __name__ == "__main__":
	query = "SELECT * FROM brands"
	cursor=db.query(query)
	for brand in cursor:
		obj = scrapping_image.scraping("\""+brand["BrandURL"]+"\"","\""+brand["BrandName"]+"\""," "," ")
		#obj.getresponse()
		#obj.extractresponse()
		#obj.specificextraction("\"+brand[Tag]+"\"","\"+brand[Attribute]+"\"","\"+brand[Value]+"\"")
		#obj.saving_image()
		obj.FilePathReader(brand["BrandName"])
		obj.datainsertion()
	print("Success")