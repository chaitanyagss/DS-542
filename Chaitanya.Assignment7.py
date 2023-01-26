#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

df = pd.read_csv(r'https://data.cityofnewyork.us/resource/jb7j-dtam.csv')

df = df.dropna()


# In[7]:


df.shape


# In[8]:


df.columns


# In[12]:


import matplotlib.pyplot as plt

#time series plot

x = df["year"]
y = df["death_rate"]

plt.plot(x,y)


# In[21]:


x = df["leading_cause"]
y = df["deaths"]

plt.figure(figsize = (5,10))
plt.barh(x, y, color = "maroon")

