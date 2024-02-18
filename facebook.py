import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv("Facebook Quarterly Results 2012-2022 - Sheet1.csv")

df['x_axis'] = df['Year'] + (df['Quarter']-1)/4
# plt.plot(df['x_axis'], df['Monthly Active Users (in millions)'], marker='.', linestyle='-',color='red',label='Monthly Active Users')
plt.plot(df['x_axis'], df['Daily Active Users (in millions)'], marker='.', linestyle='-', color='blue',label='Daily Active Users')

# Adding labels and title
plt.xlabel('Year and Quarter')
plt.ylabel('Daily Active Users (millions)')
plt.title('Facebook Daily Active Users Over Time')


# Display the graph
plt.show()
