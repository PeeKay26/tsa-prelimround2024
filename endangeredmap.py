import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import pandas as pd

# Read the CSV file into a DataFrame
file_path = "data.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# i. Remove specified columns
columns_to_remove = ['Name in French', 'Name in Spanish', 'Country codes alpha 3', 'ISO639-3 codes', 'Alternate names',
                     'Name in the language', 'Sources']
df = df.drop(columns=columns_to_remove)

# ii. Deal with null values
# You can choose a strategy based on your requirements, here we'll drop rows with any null values
df = df.dropna()

# iii. Rename columns if needed
# Example: Rename 'Degree of endangerment' to 'Endangerment Level'
df = df.rename(columns={'Degree of endangerment': 'Endangerment Level'})

import cartopy.crs as ccrs

# Assuming df is your DataFrame containing the language data

# Filter out rows with missing coordinates
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a Cartopy map
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_global()

# Define a color map based on endangerment levels
color_map = {
    'Vulnerable': 'green', 'Definitely endangered': 'yellow', 'Critically endangered': 'orange', 'Severely endangered': 'red'
}

# Plot each language with a marker based on endangerment level
for index, row in df.iterrows():
    language_name = row['Name in English']
    latitude = row['Latitude']
    longitude = row['Longitude']
    endangerment_level = row['Endangerment Level']

    # Check if latitude and longitude are not null
    if not pd.isnull(latitude) and not pd.isnull(longitude):
        ax.plot(longitude, latitude, 'o', markersize=5, color=color_map.get(endangerment_level, 'gray'), label=language_name)

# Customize the plot
ax.coastlines()

plt.title('Language Endangerment Map')
plt.show()

