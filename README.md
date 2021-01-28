# Scraping Web data Using Beautiful Soup.

![Sample Snippets Image](https://github.com/LuxTechAcademy/Web-Scraping-with-Beautiful-Soup/blob/main/DataScienceEastAfricasoup.png) 

## Common Important Commands.

#### Installing beautiful Soup

~~~python 
pip  install bs4
pip install requests

#In conda environment
conda install bs4
conda install requests
~~~

#### Importing the bs4 in the file 

~~~~python
from bs4 import BeautifulSoup
~~~

#### Importing the requests in the file 

~~~python
import requests
~~~ 

#### Creating an instance of beutifulSoup 

~~~Python
content  = requests.get("https://www.linkedin.com/jobs/search/?keywords=data%20science") 
soup = BeautifulSoup(content.text, "html.parser") 
~~~



