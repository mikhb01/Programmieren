import requests
from bs4 import BeautifulSoup

#specify url of the webpage
url = "https://en.wikipedia.org/wiki/IBM"
headers = {"User-Agent": "ExampleAndTestBot/1.0 (lengertleon@gmail.com)"}

#Send HTML GET request
response = requests.get(url, headers=headers)

#store the html content in  variable
html_content = response.text

#create a beautifulsoup object to parse to html
soup = BeautifulSoup(html_content, "html.parser")

#Display a snippet of the html content
# print(html_content[:500])

#Find all <a> tags in the HTML
links = soup.find_all("a")

# Itereate through the list of links and save the text i a txt file
with open("coursera/a_tags.txt", "w", encoding="utf-8") as writefile:
    for link in links:
        writefile.write(link.text)