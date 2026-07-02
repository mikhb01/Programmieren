import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


# get the data from the website

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text
# print(data)

# parse the html-content
soup = bs(data, "html.parser")

# identify tags
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# extracting data

# First isolating the body of the table 
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Data gets appended to each row of the table
    netflix_data = pd.concat([netflix_data, pd.DataFrame({"Date": [date], 
                                                          "Open": [open], 
                                                          "High": [high], 
                                                          "Low": [low], 
                                                          "Adj Close": [adj_close], 
                                                          "Volume": [volume]})], 
                                                          ignore_index=True)
    
# Print the data
# print(netflix_data.head())

# also possible with pandas

read_html_pandas_data = pd.read_html(url)

netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head())
