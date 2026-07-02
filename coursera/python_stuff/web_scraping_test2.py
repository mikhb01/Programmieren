import pandas as pd
import requests
URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
headers = {"User-Agent": "ExampleAndTestBot/1.0 (lengertleon@gmail.com)"}


response = requests.get(URL, headers=headers)
if response.status_code == 200:

    tables = pd.read_html(URL)
    df = tables[2] # the required table will have index 2
print(df)