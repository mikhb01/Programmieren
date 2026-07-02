import pandas as pd
data = [10, 20 ,30, 40 ,50]
s = pd.Series(data)
print(s[1:4])

#creating data frame
data = {"Name":["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 28],
        "City": ["New York", "San Francisco", "Los Angeles", "Chicago"]}
df = pd.DataFrame(data)

print(df.loc[1])

unique_dates = df["Age"].unique()
print(unique_dates)

high_above_102 = df[df["Age"] > 25]
print(high_above_102)

df.to_csv("coursera/test.csv", index=False)