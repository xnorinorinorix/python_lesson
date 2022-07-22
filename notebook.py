import pandas as pd
pd.set_option("display.max_columns", 100)
df = pd.read_csv("13112_20203_20203.csv", encoding="CP932")
df.head(3)
df.describe()
