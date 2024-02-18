import pandas as pd
import matplotlib.pyplot as plt
# df = pandas.read_csv("Twitter Yearly Results 2012-2022 - Sheet1.csv")
# plt.plot(df['Year'], df['Users (in millions)'], marker='.', linestyle='-', color='lightsteelblue',label='Active Users')
# plt.xlabel('Year and Quarter')
# plt.ylabel('Active Users (millions)')
# plt.title('Twitter Active Users Over Time')


# # Display the graph
# plt.show()

df_twitter = pd.read_csv("Twitter Yearly Results 2012-2022 - Sheet1.csv")
df_facebook = pd.read_csv("Facebook Quarterly Results 2012-2022 - Sheet1.csv")
df_facebook_avg = df_facebook.groupby('Year')['Monthly_Users'].mean().reset_index()

# Merge datasets on the 'Year' column
df_merged = pd.merge(df_twitter, df_facebook_avg, on='Year', how='inner')
df_merged = df_merged.rename(columns={'Monthly_Users': 'Facebook_Avg_Users'})

# Plotting the graph
plt.plot(df_merged['Year'], df_merged['Twitter_Users'], marker='o', linestyle='-', label='Twitter Users', color='lightsteelblue')
plt.plot(df_merged['Year'], df_merged['Facebook_Avg_Users'], marker='o', linestyle='-', label='Facebook Avg Users', color='darkmagenta')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Users (millions)')
plt.title('Twitter vs Facebook Average Users Over Time')

plt.yticks(range(0, 3000, 250))
plt.xticks(range(2012, 2023)) 

# Display the legend
plt.legend()

# Display the graph
plt.show()