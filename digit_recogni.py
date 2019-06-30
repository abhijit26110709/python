#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loading digits data
from sklearn.datasets import load_digits


# In[2]:


digit_data=load_digits() #loaded data


# In[3]:


# exploring data
dir(digit_data)


# In[4]:


# output that we want
digit_data.target_names


# In[6]:


# describing data
#digit_data.DESCR


# In[13]:


# training data
features=digit_data.data


# In[14]:


# shape
features.shape


# In[16]:


# label
label=digit_data.target


# In[17]:


label.shape


# In[18]:


# actual images
images=digit_data.images


# In[19]:


images[0] # image of zero


# In[20]:


# visual of zero
import matplotlib.pyplot as plt


# In[26]:


plt.imshow(images[8])


# In[ ]:




