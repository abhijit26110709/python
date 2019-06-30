#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loading iris data set
from sklearn.datasets import load_iris


# In[2]:


# loading into a variable
iris_data=load_iris()


# In[3]:


# describing iris data internally
dir(iris_data)


# In[4]:


# target output values --
iris_data.target_names


# In[5]:


# now attribute of features of given data
iris_data.feature_names


# In[6]:


# data with attributes
iris_features=iris_data.data


# In[7]:


# extracting label as per features
label=iris_data.target


# # showing garphs

# In[8]:


# put your code for graphs


# In[9]:


# sperating data into training and testung
from sklearn.model_selection import train_test_split


# In[11]:


train_data,test_data,train_label,test_label=train_test_split(iris_features,label,test_size=0.2)


# In[12]:


# importing KNN clf
from sklearn.neighbors import KNeighborsClassifier


# In[13]:


# now calling KNN
Kclf=KNeighborsClassifier(n_neighbors=5) # this is by default value of K


# In[14]:


# now applying training dataktr
ktrained=Kclf.fit(train_data,train_label)


# In[15]:


# now time for prediction
predict_output=ktrained.predict(test_data)


# In[16]:


predict_output


# In[17]:


test_label


# In[18]:


# calculating accuracy score
from sklearn.metrics import accuracy_score


# In[19]:


acrknm=accuracy_score(test_label,predict_output)
acrknm


# In[20]:


# calling desicion tree classifier


# In[29]:


from sklearn.tree import DecisionTreeClassifier
dclf=DecisionTreeClassifier()


# In[30]:


# training decision tree
dtrained=dclf.fit(train_data,train_label)


# In[31]:


# now predicting
dprediction=dtrained.predict(test_data)


# In[32]:


# now accuracy for decision
dacr=accuracy_score(test_label,dprediction)


# In[33]:


dacr


# In[ ]:




