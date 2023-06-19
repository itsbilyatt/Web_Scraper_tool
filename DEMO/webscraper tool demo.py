#!/usr/bin/env python
# coding: utf-8

# #  WEBSCRAPER TOOL DEMO 
# 
name:        prajyot birajdar
contact me : prajyotbirajadar1998@gmail.com1)click here:  https://github.com/itsbilyatt/webscraper/tree/main
2)download as a zip
3)extract it
4)Run this command : # pip install 'local file path'  
        
# In[1]:


# import library
from webscraper import Webscraper


# ## 1) To get soup content(it includes data with html tag) from website

# In[2]:


Webscraper('https://en.wikipedia.org/wiki/Main_Page').soup_content()


# ## 2)To get soup text (data without html tag) from website

# In[3]:


Webscraper('https://en.wikipedia.org/wiki/Main_Page').soup_text()


# ## 3)soup text  data in form of string to do string operation with that

# In[4]:


text_data=Webscraper('https://en.wikipedia.org/wiki/Main_Page').soup_text_string()


# In[5]:


text_data


# In[6]:


type(text_data)


# ## 4)soup content  data in form of string to do string operation with that 

# In[7]:


content_data = Webscraper('https://en.wikipedia.org/wiki/Main_Page').soup_content_string()


# In[8]:


content_data


# In[9]:


type(content_data)


# In[ ]:




