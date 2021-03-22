import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.read_csv('honey.csv')
 
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)
print("CLEAINING")
print(df['Value'])
 
unique_states = df['State'].unique()
all_honey = []
all_states = []
 
# with grouping
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  all_honey.append(honey_data.sum())
  all_states.append(state)
 
mid = 5e6
small = 7.5e5
 
for i in range(len(all_honey)):
    honey = all_honey[i]
    state = all_states[i]
    years = all_honey[i].keys()
 
    if(sum(honey) > mid):
         plt.plot(years, honey, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Collected")
plt.title("Sigma Boys")
plt.show()
 
for i in range(len(all_honey)):
    honey = all_honey[i]
    state = all_states[i]
    years = all_honey[i].keys()
 
    if(sum(honey) < mid and sum(honey) > small):
         plt.plot(years, honey, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Collected")
plt.title("Alpha Boys")
plt.show()
 
for i in range(len(all_honey)):
    honey = all_honey[i]
    state = all_states[i]
    years = all_honey[i].keys()
 
    if(sum(honey) < small):
         plt.plot(years, honey, label=state)
plt.xlabel("Year")
plt.ylabel("Honey Collected")
plt.title("Beta Boys")
plt.show()