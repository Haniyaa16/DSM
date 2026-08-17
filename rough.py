#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
a={'rollno':[1,2,3],'name':["red","blue","green"]}
b=pd.DataFrame(a)
print(b)


# In[2]:


a=[1,2,3,4,5]
b=pd.Series(a)
print(b)


# In[3]:


a=[1,2,3,4]
b=pd.Series(a,index=["a","b","c","d"])
print(b)


# In[4]:


import pandas as pd
a={'rollno':[1,2,3],'name':["red","blue","green"]}
b=pd.DataFrame(a)
print(b.loc[0])


# In[6]:


import pandas as pd
a={'rollno':[1,2,3],'name':["red","blue","green"]}
b=pd.DataFrame(a)
print(b.loc[:1])


# In[8]:


import pandas as pd
a={'rollno':[1,2,3],'name':["red","blue","green"]}
b=pd.DataFrame(a)
print(b.loc[2:])


# In[15]:


import pandas as pd
a=pd.read_csv('fruit.csv')
print(a)


# In[16]:


import pandas as pd
a=pd.read_csv('fruit.csv')
print(a.head(2))


# In[21]:


import pandas as pd
a=pd.read_csv('fruit.csv')
print(a.tail)


# In[25]:


a=pd.read_csv('fruit.csv')
b=a.dropna()
print(b)


# In[ ]:




