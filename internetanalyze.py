import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

df = pd.read_csv("internet-speeds-by-country-2024.csv")
# df.drop(['place','cca3','ccn3','unMember','officialName','landAreaKm','Rank'],axis=1,inplace=True)

country_name_mapping = {
    'United States': 'United States of America',
    'Guinea' : 'Guinea',
    'Republic of the Congo': 'Congo',
    'DR Congo': 'Dem. Rep. Congo',
    'Ghana': 'Ghana'

}


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

df['country'] = df['country'].replace(country_name_mapping)
merged_data = world.merge(df, how='left', left_on='name', right_on='country')

# Plot choropleth map
fig, ax = plt.subplots(1, 1)
merged_data.plot(column='InternetSpeedsFixedBroadbandDownloadSpeed', cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': "Internet Speeds (Mbps)"})


plt.title('Internet Speeds by Country')
plt.show()