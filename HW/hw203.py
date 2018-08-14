
# -*- coding: utf-8 -*-

# In[7]:


import requests
from pyquery import PyQuery as pq
from collections import namedtuple
from urllib.parse import urlparse
import sys


# In[8]:


url_base = 'https://www.imdb.com/'


# In[45]:


name_imdb = input()
query_line = (lambda name: 'find?ref_=nv_sr_fn&q={}&s=all'.format(
    name.replace(' ', '+')))(name_imdb)
# query_line


# In[48]:


url = url_base+query_line
url


# In[63]:


try:
    response = requests.get(url)
    response.encoding = 'utf-8'  # default is ISO-8859-1
    doc = pq(response.text)
    doc.make_links_absolute(base_url=response.url)
    name_href = doc(
        '.findSection > .findList tr:nth-child(1) > td.result_text > a')
#     temp=doc('.findSection > .findList > tbody')
#     print(name_href.text())
#     print(name_href.attr('href'))
    target_page_res = requests.get(name_href.attr('href'))
    target_page_res.encoding = 'utf-8'  # default is ISO-8859-1
    target_page = pq(target_page_res.text)
    # target_page.encoding('utf-8')
    # print(target_page.encoding)
    numOfMovies_text = target_page('#filmo-head-director')
    numOfMovies_text = numOfMovies_text.text()
    numOfMovies_text = numOfMovies_text[numOfMovies_text.find(
        '(')+1:numOfMovies_text.find(')')]
    print(numOfMovies_text)
    movies = target_page(
        '#filmo-head-director + .filmo-category-section > .filmo-row')
#     print(movies.text())
    for movie in movies.items():
        movie_name = movie('b > a').text()
        movie_year = movie('span.year_column').text()
        if movie_year == '':
            sep = ''
        else:
            sep = ','
        # print('{}{}{}'.format(movie_name, sep, movie_year))
        print(movie_name, movie_year, sep=sep)


except requests.HTTPError as e:
    print(e)
    sys.exit(1)
