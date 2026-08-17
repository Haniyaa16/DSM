#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
a=[1,2,3,4,5]
b=pd.Series(a)
print(b)


# In[4]:


d=pd.date_range(start='20-11-2024',end='24-11-2024')
print(d)


# In[5]:


l=[[1,'hai'],[2,'bye'],[3,'hello']]
b=pd.DataFrame(l)
print(b)


# In[6]:


import pandas as pd
a={'AGE':[1,2,3],'NAME':["red","blue","green"]}
b=pd.DataFrame(a)
print(b)


# In[7]:


import pandas as pd
a={"NAME":['a','b','c','d','e','f'],"AGE":[20,30,10,50,70,80]}
b=pd.DataFrame(a)
print("head:")
print(b.head())

print("tail:")
print(b.tail())


# In[8]:


import pandas as pd
a={'rollno':[1,2,3],'name':["red","blue","green"]}
b=pd.DataFrame(a)
print(b.loc[[1,2]])


# In[9]:


import pandas as pd
import numpy as np
d={'A':[10,20,np.nan],'B':[30,np.nan,50]}
df=pd.DataFrame(d)
print("before:")
print(df)
df=df.fillna(0)
print("after:")
print(df)


# In[ ]:




