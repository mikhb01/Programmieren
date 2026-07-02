import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= "2021-06-14"]
    revenue_data_specific = revenue_data[revenue_data.Date <= "2021-04-30"]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    #Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()


# Question 1
# Creating ticker
tesla = yf.Ticker("TSLA")

# creating a table with all history of tesla stock
tesla_data = tesla.history(period="max")

# print it
tesla_data.reset_index(inplace=True)
print(tesla_data.head())


#Question 2
# setting url
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# getting the data
html_data = requests.get(url).text

# parsing the data 
soup = BeautifulSoup(html_data, "html.parser")

# creating a table tesla_revenue
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# Table [1] is the right table for quarterly revenue
# read_html_pandas_data = pd.read_html(url)
# test_dataframe = read_html_pandas_data[1]
# soup = soup.find("tbody")[1]

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text

    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": [date], 
                                                            "Revenue": [revenue]})], 
                                                            ignore_index=True)
    
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    
print(tesla_revenue.tail())

# Question 3
# Creating gamestop ticker
gamestop = yf.Ticker("GME")

# creating a table with all history of tesla stock
gme_data = gamestop.history(period="max")

# print it
gme_data.reset_index(inplace=True)
print(gme_data.head())


#Question 2
# setting url
url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# getting the data
html_data_2 = requests.get(url2).text

# parsing the data 
soup2 = BeautifulSoup(html_data_2, "html.parser")

# create a dataframe
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])


for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text

    gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": [date], 
                                                            "Revenue": [revenue]})], 
                                                            ignore_index=True)
    
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True)

gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
    
print(gme_revenue.tail())


# Question 5
make_graph(tesla_data, tesla_revenue, "Tesla")
make_graph(gme_data, gme_revenue, "GameStop")