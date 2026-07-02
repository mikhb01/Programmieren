import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

# get data from website
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data = requests.get(url).text

# parsing the data with beautfiul soup
soup = bs(data, "html.parser")

print(soup.find_all("p"))

# print(soup.find("title"))

# creating Pandas Dataframe
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# extracting the each row
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Data gets appended to each row of the table
    amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date": [date], 
                                                          "Open": [Open], 
                                                          "High": [high], 
                                                          "Low": [low], 
                                                          "Adj Close": [adj_close], 
                                                          "Volume": [volume]})], 
                                                          ignore_index=True)
    
# Print dataframe
print(amazon_data.tail())