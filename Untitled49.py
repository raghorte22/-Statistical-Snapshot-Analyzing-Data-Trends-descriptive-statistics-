#!/usr/bin/env python
# coding: utf-8

# ### import necessary packages

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


# load the file


# In[4]:


income_df = pd.read_csv(r"D:\Data Science with AI\4th, 5th dec 2023 Inferential stats\Descriptive stats _PRACTICLE\Inc_Exp_Data.csv")


# In[5]:


income_df


# In[6]:


income_df.head()


# In[7]:


income_df.tail()


# In[8]:


# analyze the data


# In[9]:


income_df.info()


# In[11]:


income_df.shape


# In[12]:


income_df.describe().T


# In[15]:


income_df.isna().head()          #isna()-check whether the value is na or not
                                 #whether is true means value is na and false means value is not na


# In[17]:


income_df.isna().any()


# ##### no null value in the dataset

# ### what is the mean expense of a household ?

# In[18]:


income_df["Mthly_HH_Expense"].mean()


# ### what is the median household expense?

# In[19]:


income_df["Mthly_HH_Expense"].median()


# ### what is the mothly expenses for most of the household ?

# In[20]:


mth_exp_tmp = pd.crosstab(index=income_df["Mthly_HH_Expense"], columns="count")
mth_exp_tmp.reset_index(inplace=True)
mth_exp_tmp[mth_exp_tmp['count'] == income_df.Mthly_HH_Expense.value_counts().max()]


# ### Plot the Histogram to count the Highest qualified member

# In[22]:


income_df["Highest_Qualified_Member"].value_counts().plot(kind="bar")


# ### Calculate IQR(difference between 75% and 25% quartile)

# In[23]:


income_df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense")
IQR=income_df["Mthly_HH_Expense"].quantile(0.75)-income_df["Mthly_HH_Expense"].quantile(0.25)
IQR


# In[26]:


#Calculate Variance for first 3 columns.
pd.DataFrame(income_df.iloc[:,0:4].var().to_frame()).T


# In[28]:


#11.Calculate the count of Highest qualified member.
income_df["Highest_Qualified_Member"].value_counts().to_frame().T


# ### plot the histogram to count the no_of _earning_members

# In[30]:


income_df["No_of_Earning_Members"].value_counts().plot(kind="bar")


# ### Suppose you have option to invest in Stock A or Stock B. The stocks • have different expected returns and standard deviations. The expected return of Stock A is 15% and Stock B is 10%. Standard Deviation of the returns of these stocks is 10% and 5% respectively.¶

# In[31]:


#here we need to calculate the coeff of variation

Coeff_of_var_StockA=10/15
print(Coeff_of_var_StockA)
Coeff_of_var_StockB=5/10
print(Coeff_of_var_StockB)


# In[ ]:




