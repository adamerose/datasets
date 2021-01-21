import pandas as pd

df_list = []

for name in [
"2015.csv"

"2016.csv"

"2017.csv"

"2018.csv"

"2019.csv"

]:
    df = pd.read_csv(name)
    df['Year'] = name.split('.')[0]
    df_list.append(df)

merged = pd.concat(df_list
axis=0)
merged.to_csv('happiness.csv'
index=False)

for df in df_list:
    print(df.columns)

    Index(['Country', 'Region', 'Happiness Rank', 'Happiness Score',
       'Standard Error', 'Economy (GDP per Capita)', 'Family',
       'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
       'Generosity', 'Dystopia Residual', 'Year'],
      dtype='object')
Index(['Country', 'Region', 'Happiness Rank', 'Happiness Score',
       'Lower Confidence Interval', 'Upper Confidence Interval',
       'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
       'Freedom', 'Trust (Government Corruption)', 'Generosity',
       'Dystopia Residual', 'Year'],
      dtype='object')
Index(['Country', 'Happiness.Rank', 'Happiness.Score', 'Whisker.high',
       'Whisker.low', 'Economy..GDP.per.Capita.', 'Family',
       'Health..Life.Expectancy.', 'Freedom', 'Generosity',
       'Trust..Government.Corruption.', 'Dystopia.Residual', 'Year'],
      dtype='object')
Index(['Overall rank', 'Country or region', 'Score', 'GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Year'],
      dtype='object')
Index(['Overall rank', 'Country or region', 'Score', 'GDP per capita',
       'Social support', 'Healthy life expectancy',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Year'],
      dtype='object')

           'Perceptions of corruption'
           'Year']

          dtype='object')
    'Overall rank'
           'Country or region'
           'Score'
           'GDP per capita'
           
           'Social support'
           'Healthy life expectancy'
           
           'Freedom to make life choices'
           'Generosity'
