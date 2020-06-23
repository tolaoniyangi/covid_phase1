#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd
from datetime import datetime,date


# In[2]:


df_original = gpd.read_file('P1_Daily_COVID_NYC_Date.shp')
df_original.head()


# In[3]:


df_original.plot()


# In[4]:


df_original.columns


# In[5]:


df_selected = df_original[['MODZCTA','NEIGHBORHO','BOROUGH_GR','COVID_CASE','Per_Pos','Date_Conv','geometry']].copy()
df_selected.head()


# In[6]:


df = df_selected.rename(columns={"MODZCTA": "Zip Code", 
                   "NEIGHBORHO": "Neighborhood",
                   "BOROUGH_GR": "Borough",
                   "COVID_CASE": "Number of COVID Cases",
                   "Per_Pos": "Percentage Positive",
                   "Date_Conv": "Date",
                })

df.head()


# In[7]:


# df['Date'] = pd.to_datetime(df['Date']).dt.date
df['Date'] = pd.to_datetime(df['Date']).dt.normalize()

df.head()


# In[15]:


df["Date"] = df["Date"].astype(str)
df.dtypes


# In[22]:


df.to_file('selected-covid-data-phase-one.geojson', driver="GeoJSON")

