import pandas as pd

df = pd.read_csv('Characters.csv', sep=';', encoding="latin1")
df.to_csv('harry_potter_characters.csv', index=False)
