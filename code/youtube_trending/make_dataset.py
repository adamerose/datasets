import os

import pandas as pd

from pandasgui import show

json_list = [
    "FR_category_id.json",
    "GB_category_id.json",
    "IN_category_id.json",
    "JP_category_id.json",
    "KR_category_id.json",
    "MX_category_id.json",
    "RU_category_id.json",
    "US_category_id.json",
    "BR_category_id.json",
    "CA_category_id.json",
    "DE_category_id.json",
]

csv_list = [
    "CA_youtube_trending_data.csv",
    "DE_youtube_trending_data.csv",
    "FR_youtube_trending_data.csv",
    "GB_youtube_trending_data.csv",
    "IN_youtube_trending_data.csv",
    "JP_youtube_trending_data.csv",
    "KR_youtube_trending_data.csv",
    "MX_youtube_trending_data.csv",
    "RU_youtube_trending_data.csv",
    "US_youtube_trending_data.csv",
    "BR_youtube_trending_data.csv",
]

country_abbrev = {'BR': 'Brazil',
                  'CA': 'Canada',
                  'DE': 'Germany',
                  'FR': 'France',
                  'GB': 'United Kingdom',
                  'IN': 'India',
                  'JP': 'Japan',
                  'KR': 'South Korea',
                  'MX': 'Mexico',
                  'RU': 'Russia',
                  'US': 'United States'}

df_list = []
for csv_name, json_name in zip(csv_list, json_list):
    csv_path = os.path.join('raw', csv_name)
    json_path = os.path.join('raw', json_name)

    print(csv_name)

    videos = pd.read_csv(csv_path, encoding="ISO-8859-1")
    categories_json = pd.read_json(json_path)

    videos = videos.rename(columns={
        'publishedAt': 'published_at',
        'channelId': 'channel_id',
        'channelTitle': 'channel_title',
        'categoryId': 'category_id',

    })
    categories_list = []
    for index, row in categories_json.iterrows():
        category_id = int(row['items']['id'])
        category_name = row['items']['snippet']['title']
        categories_list.append(
            {'category_id': category_id, 'category_name': category_name})

    categories_df = pd.DataFrame(categories_list)

    df = pd.merge(videos, categories_df, on='category_id', how='left')

    df['country_code'] = csv_name[0:2]
    df['country'] = country_abbrev[csv_name[0:2]]
    df_list.append(df)

merged = pd.concat(df_list, axis=0)


merged.to_csv('youtube_trending.csv', index=False)
merged.query('country == "United States"').to_csv('youtube_trending_usa.csv', index=False)
