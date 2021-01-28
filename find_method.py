"""
Find Method that looks for a specific element in the webpage 

- find 
- find_all
- Loopsing through elements to print just the text content
"""

#Import the  library 7
from bs4 import BeautifulSoup 

with open("index.html", "r") as html_file:
	content = html_file.read()
	"""If you want to print content run: print(content)"""

	soup = BeautifulSoup(content, "lxml")
	"""The above code makes the element to appear as it is in the website"""
	tag = soup.find("h1")
	print(tag)
	print("***tags***")
	""" Note that the find method just gets the first element and stop the execution.
        To get all element change the method to find_all 
    """
	tags  = soup.find_all("h1")
	#printing the text in the tags 
	for tagstext in tags:
		print(tagstext.text)

	







