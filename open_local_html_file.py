"""
This is basic code that will open local markup file, store it content in a variable call content and print the output
"""
#Import the  library 7

from bs4 import BeautifulSoup 

with open("index.html", "r") as html_file:
	content = html_file.read()
	"""If you want to print content run: print(content)"""


	soup = BeautifulSoup(content, "lxml")
	"""The above code makes the element to appear as it is in the website"""
	print(soup.prettify())