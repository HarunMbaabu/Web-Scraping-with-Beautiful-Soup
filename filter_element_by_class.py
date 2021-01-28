"""
It is important to note that class is in built in python, hence when selecting a html element 
and filtering by class us class_, beautiful soup will understand with want an element with a specific class name
"""

"""
Example
"""

#Import the  library 7
from bs4 import BeautifulSoup 

with open("index.html", "r") as html_file:
	content = html_file.read()
	"""If you want to print content run: print(content)"""

	soup = BeautifulSoup(content, "lxml")
	tags = soup.find("h1", class_="python") 
	print(tags)
	#View  what is in tags
	for texts in tags:
		print(texts)