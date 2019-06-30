#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# In[3]:


# now loading IRIS data only
iris=load_iris()


# In[4]:


dir(iris) #exploring variable


# In[ ]:





# In[7]:


iris.feature_names #this are feature names


# In[9]:


# labels or answer
iris.target_names


# In[12]:


# actual data with attributes is
features=iris.data
features.shape


# In[13]:


type(features)


# In[17]:


# now time for label data that will be exactly same as number of features data
label=iris.target
label.shape


# In[21]:


SL=features[0:,0]


# In[22]:


SW=features[0:,1]


# In[31]:


plt.xlabel("length")
plt.ylabel("width")
plt.scatter(SL,SW)
plt.scatter(features[0:,2],features[0:,3],label="petal_data",marker='x')
plt.legend()


# In[ ]:


# now time for seprating data nto 2 category
#1.------training data
#2.------ testing data---questions
from sklearn.model_selection import train_test_split
train_data,test_data,label,label_test=train_test_split(features,label,test_size=0.1)


# In[ ]:


# calling decisiontree classiier
clf=DecisionTreeClassifier()


# In[ ]:


# now time for training clf
trained=clf.fit(train_data,label_train)


# In[ ]:


# now predicting flowers
predicted_flowers=trained.predict(test_data)


# In[ ]:


predicted_flowers # algo answer


# In[ ]:


label_test # actual answer


# In[ ]:


# find accuracy score
accuracy_score(label_test,predicted_flowers)


# In[ ]:




