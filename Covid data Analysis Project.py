#!/usr/bin/env python
# coding: utf-8

# #    Covid-19 Data Analysis 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime 


# In[2]:


covid_df  =pd.read_csv("D:/Covid-India/covid_19_india.csv")


# In[3]:



covid_df.head(10)


# In[4]:


covid_df.drop(["Sno"], axis=1)


# In[5]:


covid_df.tail()


# In[6]:


covid_df.columns


# In[7]:


covid_df.info()


# In[8]:


covid_df.describe()


# In[9]:


covid_df.isnull().sum()


# In[10]:


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis=1)


# In[11]:


covid_df.head()


# In[12]:


covid_df.head()


# In[25]:


covid_df


# In[15]:


#Active Cases

covid_df['Active_Cases'] =covid_df['Confirmed'] - (covid_df['Cured']+covid_df['Deaths'])
covid_df.tail()                                   


# In[26]:


statewise = pd.pivot_table(covid_df, values = ['Confirmed', 'Deaths', "Cured"], index = "State/UnionTerritory", aggfunc = max)


# In[27]:


statewise['Recovery Rate'] = statewise['Cured']*100/statewise['Confirmed']


# In[28]:


statewise['Mortality Rate'] = statewise['Deaths']*100/statewise['Confirmed']


# In[29]:


statewise = statewise.sort_values(by = "Confirmed", ascending = False)


# In[30]:


statewise.style.background_gradient(cmap = "cubehelix")
                                    


# In[32]:


#Top 10 Active Cases States
top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by =  ['Active_Cases'],  ascending  = False). reset_index()


# In[33]:


fig  =plt.figure(figsize  =(16,9))


# In[34]:


plt.title("Top 10  States with most active cases in India")


# In[35]:


ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = 'red')


# In[36]:


#Top 10 Active Cases States
top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by =  ['Active_Cases'],  ascending  = False). reset_index()
fig  =plt.figure(figsize  =(16,9))
plt.title("Top 10  States with most active cases in India")
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_Cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = 'white')
plt.x_label("STATES")
plt.y_label("Total Active Cases")
plt.show()



# In[37]:


#Top 10 states eith highest deaths 


# In[38]:


top_10_deaths  =covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths', 'Date']]. sort_values(by =['Deaths'], ascending= False).reset_index()
fig = plt.figure(figsize = (18,5))
plt.title("Top 10 states with most Deaths", size = 25)
ax = sns.barplot(data = top_10_deaths.iloc[:12], y = "Deaths", x= "State/UnionTerritory", linewidth = 2, edgecolor = 'white')
plt.x_label("STATES")


# In[ ]:





# In[ ]:




