#!/usr/bin/env python
# coding: utf-8

# In[45]:


from bs4 import BeautifulSoup
import requests
# from lxml import etree
import numpy as np
import pandas as pd
import datetime
import json


# In[67]:


with open('/Users/jadisy/Documents/GitHub/instagram-crawler/output.json', 'r') as f:
    distros_dict = json.load(f)

list_likes = []
    
for distro in distros_dict:
    url = distro['key']
    data = requests.get(url).text
    soup = BeautifulSoup(data)
    for tag in soup.find_all('meta', property='og:description'):
        list_likes.append(tag['content'])


# In[82]:


df_likes = pd.DataFrame()
df_likes['list_likes'] = list_likes
df_likes_num = df_likes['list_likes'].str.split(pat=' ', n=3, expand=True)
df_content_brief = df_likes['list_likes'].str.split(pat=':', n=2, expand=True)


# In[83]:


df_likes_num.head()


# In[84]:


df_content_brief.head()


# In[85]:


df_distro = pd.DataFrame.from_dict(distros_dict)
df_distro['num_likes'] = df_likes_num[0]
df_distro['num_comms'] = df_likes_num[2]
df_distro['content_brief'] = df_content_brief[1]


# In[86]:


df_distro.head()


# In[87]:


now = datetime.datetime.now()
df_distro.to_csv(r'/Users/jadisy/Documents/output_ins_{}.csv'.format(now.strftime("%Y-%m-%d %H-%M")))

