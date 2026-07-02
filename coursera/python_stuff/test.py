# # import numpy as np
import pandas as pd

# data = {"Artist": ["Michael Jackson"], "Length": [2], "Genre": ["Rock"], "Country": ["USA"]}
# df = pd.DataFrame(data)

# print(df)

# y = df(["Artist"])
# print(y)

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

tables = pd.read_html(URL, storage_options=header)

df = tables[0]
print(df)