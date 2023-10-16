import pandas as pd
import numpy as np
import re
import string

# processing the text by removing null values and converting the column to string
df = pd.read_csv("fkart_rev.csv")
df['comment'].replace('', np.nan, inplace=True)
df.dropna(subset=['comment'], inplace=True)
df["comment"] = df["comment"].astype(str)

text = []

# processing the text output by removing unnecessary words
for i, row in df.iterrows():
    a = row['comment'].removesuffix('READ MORE')
    # a = a.translate(str.maketrans('', '', string.punctuation))
    text.append(a)

# adding the processed text back to the original dataframe
column_values = pd.Series(text)
df.insert(loc=3, column='text', value=column_values)

print(df.head())

# exporting the new dataframe to a csv file
df.to_csv('flip_clean.csv', index=False)