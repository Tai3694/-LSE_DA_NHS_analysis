#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import the necessary packages.
import pandas as pd


# In[4]:


# Read CSV file from the current working directory.
ad = pd.read_csv('actual_duration.csv')

ar = pd.read_csv('appointments_regional.csv')

nc = pd.read_excel('national_categories.xlsx')


# In[5]:


# View the DataFrame
ad.head()


# In[6]:


# View the DataFrame
ar.head()


# In[7]:


# View the DataFrame
nc.head()


# In[8]:


#Getting the number of columns and rows for ad DataFrame
ad.info


# In[9]:


#Determing the column names
print(ad.columns)


# In[10]:


#Looking at the datatypes
ad.dtypes


# In[11]:


#Finding is missing value
ad.isna()


# In[12]:


#Finding the total count of missing value per column 
ad.isna().sum()


# In[13]:


#Gettingthe number of columns and rows for the ar DataFrame
ar.info


# In[14]:


#Determing the column names
print(ar.columns)


# In[15]:


#Looking at the datatypes
ar.dtypes


# In[16]:


#Finding is missing value
ar.isna()


# In[17]:


#Finding the total count of missing value per column 
ar.isna().sum()


# In[18]:


#giving the number of columns and rows for nc DataFrame
nc.info


# In[19]:


#Determing the column names
print(nc.columns)


# In[20]:


#Looking at the datatypes
nc.dtypes


# In[21]:


#Finding is missing value
nc.isna()


# In[22]:


#Finding the total count of missing value per column 
nc.isna().sum()


# In[23]:


#Descriptive statistics for ad DataFrame
ad.describe()


# In[24]:


#Descriptive statistics for ad DataFrame
ar.describe()


# In[25]:


#Descriptive statistics for ad DataFrame
nc.describe()


# In[30]:


#Counting the number of locations in the DataFrame
ad['sub_icb_location_name'].value_counts()


# In[34]:


#Repeat counting the number of locations in the different DataFrame
nc['sub_icb_location_name'].value_counts()


# In[49]:


#Five locations with highest number of records using sum
ad.groupby('sub_icb_location_name', 
           as_index=False).sum().nlargest(n=5, 
                                          columns='count_of_appointments')


# In[59]:


#Using nc DataFrame to work out question 3c
#Working out the number of service setting
nc.info()


# In[58]:


#Using nc DataFrame to work out question 3c
#Working out the number of service setting
nc['service_setting'].nunique()


# In[60]:


#Working out the number of context types
nc['context_type'].nunique()


# In[61]:


#Working out the number of national categories
nc['national_category'].nunique()


# In[63]:


#Working out the number of appointment statuses
#Need to switch to using the ar DataFrame
ar['appointment_status'].nunique()

