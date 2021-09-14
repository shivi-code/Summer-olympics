#!/usr/bin/env python
# coding: utf-8

# #  Summer Olympics Data Analysis Assignment
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("summer.csv")
df.head()


# In[3]:


df.shape


# #  1.In how many cities Summer Olympics is held so far?
# 

# In[4]:


len(df['City'].unique())


# # 2. Which sport is having most number of Gold Medals so far? (Top 5)

# In[5]:


df[df['Medal']=='Gold'].Sport.value_counts().head().plot(x = 'Sport', y = ' Gold Medal', kind = 'bar', figsize = (10,5))


# # 3. Which player has won most number of medals? (Top 5)
# 

# In[6]:


df.Sport.value_counts().head().plot(x = 'Player', y = 'Medal', kind = 'bar', figsize = (10,5))


# # 4. Which player has won most number of medals? (Top 5)

# In[6]:


df.Athlete.value_counts().head().plot(x = 'Player', y = 'Medal', kind = 'bar', figsize = (10,5))


# # 5. Which player has won most number Gold Medals of medals? (Top 5)

# In[7]:


df[df.Medal=='Gold'].Athlete.value_counts().head().plot(x = 'Player', y = ' Gold Medal', kind = 'bar', figsize = (10,5))


# # 6. In which year India won first Gold Medal in Summer Olympics?

# In[8]:


df2 = df[df.Medal =='Gold']
min(df2[df2.Country=='IND'].Year)


# # 7. Which event is most popular in terms on number of players? (Top 5)

# In[9]:


df['Event'].value_counts().head().plot(x = 'Event', y = 'Player', kind = 'bar', figsize = (10,5))


# # 8. Which sport is having most female Gold Medalists?

# In[10]:


df2 = df[df.Medal=='Gold']
df2[df2.Gender== 'Women'].Sport.value_counts().head().plot(x = 'Event', y = 'Player', kind = 'bar', figsize = (10,5))

