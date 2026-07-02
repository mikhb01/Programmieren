import yfinance as yf
import pandas as pd
import json

amd = yf.Ticker("AMD")

with open('coursera/python_stuff/labs/amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(amd_info)

print("Country: ", amd_info["country"])
print("Sector: ", amd_info["sector"])

amd_share_price_data = amd.history(period="max")
print(amd_share_price_data.head())