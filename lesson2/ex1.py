
# coding: utf-8

# In[56]:

import requests
from pyquery import PyQuery as pq


# In[57]:

response=requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone')


# In[58]:

result=pq(response.text)


# In[59]:

# response.text


# In[60]:

result('body > div.container > div > div.col-md-9 > div.jumbotron > h1').text()


# In[61]:

result('body > div.container > div > div.col-md-9 > div.jumbotron > p').text()


# In[62]:

items=result('body > div.container > div > div.col-md-9 > div.row > div > div > div.caption > h4:nth-child(2) > a')


# In[68]:

items


# In[ ]:



