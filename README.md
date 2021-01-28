# Scraping Web Data Using Beautiful Soup.

![Sample Snippets Image](https://github.com/LuxTechAcademy/Web-Scraping-with-Beautiful-Soup/blob/main/DataScienceEastAfricasoup.png) 

## Common Methods & Commands You should Know.

#### Installing beautiful Soup

~~~python 
pip  install bs4
pip install requests

#In conda environment
conda install bs4
conda install requests
~~~

~~~python
#Importing the bs4 in the file 
from bs4 import BeautifulSoup

#Importing the requests in the file 
import requests

#Creating an instance of beutifulSoup 
content  = requests.get("https://www.linkedin.com/jobs/search/?keywords=data%20science") 
soup = BeautifulSoup(content.text, "html.parser") 

~~~

---

~~~python
soup.prettify() 

#Navigating tag names 
soup.title
soup.h1
~~~


