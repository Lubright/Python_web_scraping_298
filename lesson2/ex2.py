
# coding: utf-8

# In[90]:

import requests
from pyquery import PyQuery as pq


# In[91]:

response=requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone')


# In[92]:

result=pq(response.text)
result.make_links_absolute(base_url=response.url)


# In[96]:

items=result('#side-menu > li:nth-child(n+2) > a')


# In[100]:

for item in items.items():
#     print(item.text(),':',item.attr('href'))
    sub_item_content=pq(item.attr('href'))
    sub_item_content.make_links_absolute(base_url=response.url)
    sub_items=sub_item_content('#side-menu > li.active > ul > li > a')
    for e in sub_items.items():
#         print(e.text(),':',e.attr('href'))
        target_content=pq(e.attr('href'))
        target_item=target_content('body > div.container > div > div.col-md-9 > div > div > div')
        for e2 in target_item.items():
            print(e2.text())
    


# In[62]:

items=result('body > div.container > div > div.col-md-9 > div.row > div > div > div.caption > h4:nth-child(2) > a')


# In[68]:

items


# In[ ]:



