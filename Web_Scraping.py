What is Web Scrapping
The internet is full of huge amount of data which can be used for different purposes. 
To collect this data we need to know how to scrape data from a website.

Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or 
in a database.

In this section, we will use beautifulsoup and requests package to scrape data. 
The package version we are using is beautifulsoup 4.



To start scraping websites you need requests, beautifoulSoup4 and a website.


exit()
pip install requests
pip install beautifulsoup4

python #in terminal


To scrape data from websites, basic understanding of HTML tags and CSS selectors is needed. 
We target content from a website using HTML tags, classes or/and ids. 
Let us import the requests and BeautifulSoup module


import requests
from bs4 import BeautifulSoup

Let us declare url variable for the website which we are going to scrape.
    

import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/?utm_source=chatgpt.com'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful




Using beautifulSoup to parse content from the page


import requests
from bs4 import BeautifulSoup
url = 'https://books.toscrape.com/?utm_source=chatgpt.com'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)



import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# get all books on the page
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(title, "-", price)


-----------------------------------------------

When to use web scraping

Use scraping when:

there is no API
data is public on webpages
you need webpage content itself
you want prices/articles/reviews/listings

Example:

scraping product prices
scraping news headlines
scraping tables from Wikipedia



----------------------------------------------

API example use cases

Good for:

weather data
stock prices
maps
user accounts
government/open datasets
sports scores

Examples:

OpenWeather API
GitHub REST API
World Bank API



---------------------------------------------------------------------------------------------


FInd an example of Web scraping