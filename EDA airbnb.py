#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis: Airbnb Listings
# 

# ## Importing libraries, loading dataset and simple exploration
# 

# In[1]:


#importing necessery libraries for future analysis of the dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.express as px
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


# In[2]:


df= pd.read_csv('listings1.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# # Data Cleaning
# # check dublicates and null values

# In[6]:


df.duplicated().sum()


# In[7]:


df.isnull().sum()


# ### The following columns have null values:host_name, last_review, reviews_per_month, license. The last_review column is a date column, so the most likely solution for it is to drop it. The reviews_per_month column is required to find trends between data, so it is best to append missing values in 0. The license column will be dropped as well.
# 
# 

# ## drop dublicates and null columns

# In[8]:


df.drop(['neighbourhood_group','last_review','license'],axis=1,inplace=True)
df.sample()


# In[9]:


#fill nan values 
df.fillna(0,inplace=True)


# In[10]:


#check nulls
df.isnull().sum()


# In[11]:


df.describe()


# ###### We need to group the trends according to neighbourhood, neighbourhood_group, room_type or property_type

# In[12]:


#make grouplist between neighbourhood and host_id
df2=df.groupby('neighbourhood')['host_id'].count()


# In[13]:


df1=pd.DataFrame(df2)
df1.reset_index(inplace=True)
df1


# In[14]:


px.bar(
    df1,
    x= df1['neighbourhood'].unique(),
    y= df1['host_id'],
    color = df['neighbourhood'].unique(),
    labels = {'x': 'Neighbourhood', 'y':'Total numbers'},
    title = 'Total Numbers by Neighbourhood' ,width=2000   )


# ###### From this plot we found that Historisch Centrum have the most no of hosts and their is neighbourhood has 1 host like polder

# In[15]:


fig=df.plot(kind='scatter', x='longitude', y='latitude', c='price',
                  cmap=plt.get_cmap("rocket"), colorbar=True, alpha=0.2, figsize=(10,8))
fig.legend()


# ###### Observations about the mapping of yearly available, different priced properties along different latitudes and longitudes:
# The maximum priced, highly available properties are concentrated in the northwest
# 
# The minimum priced, highly available properties are concentrated in the center (least number of bright red plots),
# 
# The least available properties are found in north and south

# In[16]:


# make a group between room type and price to find relation between them
average = df.groupby(['room_type','neighbourhood'])['price'].mean().reset_index()
average


# In[17]:


px.bar(average,
       x = 'neighbourhood',
       y = 'price',
       color = 'room_type',
       labels={'room_type': 'Room Type', 'price': 'Average Price', 'neighbourhood':'Neighbourhood'},
       title='Average Price by Room Type and Neighbourhood',
       facet_row = 'room_type',
       category_orders = {'price':'descending'},
       height = 1000,
       width = 1000
      )


# ###### we observe that the most trend is entire home
# the highest price is in polder and that is because it has minimum no of rooms
# the lowest price is in luchtabl 
# 
# #### the least used is hotel rooms and shared rooms
# 
# #### the private room has average use
# the highest price is in sint-andris
# 

# In[18]:


fig = px.scatter(
    df,
    x='latitude',
    y='longitude',
    color='room_type',
    size='price',
    labels={'room_type': 'Room Type', 'price': 'Price'},
    title='Airbnb Map by Room Type and Price',
)

fig.show()


# ###### this plot show the price of every room type in the neighbours on map

# In[19]:


# know the average priceof each neighbourhood
average2 = df.groupby('neighbourhood')['price'].mean().reset_index()
average2


# In[20]:


px.bar(average,
       x = 'neighbourhood',
       y = 'price',
       color = 'neighbourhood',
       labels={'price': 'Average Price', 'neighbourhood':'Neighbourhood'},
       title='Average Price Neighbourhood',
       category_orders = {'price':'descending'},
       height = 1000,
       width = 1000
      )


# ###### plot to show the average price of every neighbourhood

# ### know the most hosts

# In[21]:


##show all the top_host values
bestrenter=df['host_id'].value_counts().head(15)
bestrenter


# In[22]:


#show all the top_host values
bestrenter_df=pd.DataFrame(bestrenter)
bestrenter_df.reset_index(inplace=True)
bestrenter_df


# In[23]:


bestrenter_df.rename(columns={'index':'Host_ID', 'host_id':'Count'}, inplace=True)
bestrenter_df


# In[24]:


fig1=sns.barplot(x=bestrenter_df["Host_ID"], y=bestrenter_df["Count"], data=bestrenter_df, palette="rocket")
fig1.set_title('Hosts with the most listings in NYC')
fig1.set_ylabel('Count of listings')
fig1.set_xlabel('Host IDs')
fig1.set_xticklabels(fig1.get_xticklabels(), rotation=45)
sns.set(rc={'figure.figsize':(30,10)})


# ###### we know the most host renter who is490705947 and the lowest one in top 15 is 3977485597

# Conclusion:
# 1-When prices were analysed across different neighbourhoods and neighbourhood_gps, a considerable range was found. Amandus - Atheneum was the most expensive and polder was the cheapest
# 2-the top 10 most reviewed listings are mostly private rooms that are either in Amandus - Atheneum	 or Borgerhout Extra Muros	 with at least a ★4.41 rating. The average price per night among these is $50 which is a price of average density among the neighbourhood.
# 

# ##### This EDA helps us to learn about:
# 1) The occurrence of prices
# 
# 2) How to save company resources and costs by knowing which locations and prices to make more available
# 
# 3) How to price newly introduced rooms
# 
# 4) This is also helpful to understand analytics better and how to offer better deals to potential cutomers
# 
# ## The End

# In[ ]:




