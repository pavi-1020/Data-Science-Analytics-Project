
# coding: utf-8

# UpX Academy - Proect - Question - Section1- On delays

# In[54]:

import pandas as pd    
import numpy as np
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[2]:

#Read the data
airline_data = pd.read_csv('C:/Course/Projects/flight_data.csv')


# In[5]:

#Which Airport has the highest arrival and departure delay and what is the comparison with other airports
mean_depdelay = airline_data.groupby(['origin']).dep_delay.mean()
mean_arrdelay = airline_data.groupby(['origin']).arr_delay.mean()
N=3
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars
fig, ax = plt.subplots(figsize=(12, 8))
rects1 = ax.bar(ind,mean_depdelay, width, color='c')
rects2 = ax.bar(ind+width,mean_arrdelay, width, color='g')
ax.set_ylabel('Mean Values')
ax.set_title('Mean Departure and Arrival delay by Airport')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('EWR', 'JFK', 'LGA'))
ax.legend((rects1[0], rects2[0]), ('Departure Delay', 'Arrival Delay'))
def autolabel(rects):
     for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%.2f' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.show()


# In[73]:

#Which month of the year sees maximum delays?
month_wise_dep_delay = airline_data.groupby(['month']).dep_delay.mean()
month_wise_arr_delay = airline_data.groupby(['month']).arr_delay.mean()
month_wise_arr_delay
N=12
ind = np.arange(N)  # the x locations for the groups
width = 0.35      # the width of the bars
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(20, 10))
rects1 = ax.bar(ind,month_wise_dep_delay, width, color='c')
rects2 = ax.bar(ind+width,month_wise_arr_delay, width, color='g')
ax.set_xticks(ind + width / 2)
ax.set_ylabel('Mean Delay')
ax.set_title('Mean Departure and Arrival delay by Month')
ax.set_xticklabels(('January', 'February', 'March','April', 'May', 'June','July', 'August', 'September','October', 'November', 'December'))
ax.legend((rects1[0], rects2[0]), ('Departure Delay', 'Arrival Delay'))
def autolabel(rects):
     for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%.2f' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.show()


# In[83]:

#Which hour of the day sees most delays
hour_wise_dep_delay = airline_data.groupby(['hour']).dep_delay.mean()
hour_wise_arr_delay = airline_data.groupby(['hour']).arr_delay.mean()
hour_wise_dep_delay = hour_wise_dep_delay.dropna()
hour_wise_arr_delay = hour_wise_arr_delay.dropna()
key_list = []
for k in hour_wise_arr_delay.keys():
    key_list.append(str(k))
val = hour_wise_dep_delay.count()
ind = np.arange(val)  # the x locations for the groups
width = 0.35      # the width of the bars
fig, ax = plt.subplots(figsize=(20, 10))
rects1 = ax.bar(ind,hour_wise_dep_delay, width, color='c')
rects2 = ax.bar(ind+width,hour_wise_arr_delay, width, color='g')
ax.set_xticks(ind + width / 2)
ax.set_ylabel('Mean Delay')
ax.set_title('Mean Departure and Arrival delay by Hour of the day')
ax.set_xticklabels(key_list)
ax.legend((rects1[0], rects2[0]), ('Departure Delay', 'Arrival Delay'))
def autolabel(rects):
     for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%0.2f' % height,
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()


# In[11]:

#Which Carrier has highest delay
carrier_wise_dep_delay = airline_data.groupby(['carrier']).dep_delay.mean()
carrier_wise_arr_delay = airline_data.groupby(['carrier']).arr_delay.mean()
carrier_wise_dep_delay = carrier_wise_dep_delay.dropna()
carrier_wise_arr_delay = carrier_wise_arr_delay.dropna()
key_list = []
for k in carrier_wise_arr_delay.keys():
    key_list.append(str(k))
#print(key_list)
val = carrier_wise_dep_delay.count()
ind = np.arange(val)  # the x locations for the groups
width = 0.35      # the width of the bars
fig, ax = plt.subplots(figsize=(20, 10))
rects1 = ax.bar(ind,carrier_wise_dep_delay, width, color='c')
rects2 = ax.bar(ind+width,carrier_wise_arr_delay, width, color='g')
ax.set_xticks(ind + width / 2)
ax.set_ylabel('Mean Delay')
ax.set_title('Mean Departure and Arrival delay by Carrier')
ax.set_xticklabels(key_list)
ax.legend((rects1[0], rects2[0]), ('Departure Delay', 'Arrival Delay'))
def autolabel(rects):
     for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%0.2f' % height,
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
plt.show()


# In[60]:

# Top 8 Destination with lowest and highest Arrival delay
dest_wise_arr_delay = airline_data.groupby(['dest']).arr_delay.mean()
dest_wise_arr_delay = dest_wise_arr_delay.dropna()
dest_wise_arr_delay.sort()
lowest_8 = dest_wise_arr_delay[:8]
#print(lowest_8)
highest_8 = dest_wise_arr_delay[96:]
#print(highest_8)
top_bottom_8= lowest_8.append(highest_8)
#print(top_bottom_8)
key_list = []
for k in top_bottom_8.keys():
    key_list.append(str(k))
#print(key_list)
val = top_bottom_8.count()
ind = np.arange(val)  # the x locations for the groups
width = 0.35      # the width of the bars
fig, ax = plt.subplots(figsize=(20,10))
rects2 = ax.bar(ind+width,top_bottom_8, width, color='g')
ax.set_xticks(ind + width / 2)
ax.set_ylabel('Mean Delay')
ax.set_title('Mean Arrival delay by Destination')
ax.set_xticklabels(key_list)
#x.legend(rects2,'Arrival Delay')
def autolabel(rects):
     for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                '%0.2f' % height,
                ha='center', va='bottom')
autolabel(rects2)
plt.show()


# In[ ]:




# In[ ]:




# In[ ]:



