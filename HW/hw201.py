
# coding: utf-8

# In[109]:


import requests
from pyquery import PyQuery as pq
from collections import namedtuple
from urllib.parse import urlparse


# In[110]:


def cal_money(money, receipt_list):
    sum1 = 0
    for receipt in receipt_list:
        sum1 += round((receipt.money *
                       money[receipt.money_type+'_'+receipt.date]), 0)
    return int(sum1)


# In[111]:


url = 'https://rate.bot.com.tw/xrt/history?Lang=zh-TW'
Receipt = namedtuple('Receipt', ['date', 'money_type', 'money'])
Receipt_list = []


# In[112]:


url_parse = urlparse(url)
url_base = '{}://{}'.format(url_parse.scheme, url_parse.netloc)
target_url = url_base+'/xrt/all/'


# In[113]:


while True:
    try:
        line = input()
        line = [e for e in line.split(' ') if e != '']
        receipt = Receipt(line[0].replace('/', '-'), line[1], float(line[2]))
        # print(receipt)
#         print(receipt.date)
        Receipt_list.append(receipt)

    except EOFError as e:
        break
    except:

        continue


# In[114]:


money_dict = {}
for receipt in Receipt_list:
    # print(target_url+receipt.date)
    response = requests.get(target_url+receipt.date)
#     print(response.text)
    doc = pq(response.text)
    tr = doc('body > div.page-wrapper > main > div:nth-child(4) > table > tbody > tr')
    for row in tr.items():
        #         print(row('div.visible-phone.print_hide').text())
        money_type = row('div.visible-phone.print_hide').text()
        money_type = money_type[money_type.find('(')+1:money_type.find(')')]
        # print(money_type)
#         print(row('td:nth-child(5)').text())
        if money_type == receipt.money_type and money_type not in money_dict:
            money_dict[money_type+'_' +
                       receipt.date] = float(row('td:nth-child(5)').text())
            break


# In[115]:


money_dict


# In[116]:


print('{:d}'.format(cal_money(money_dict, Receipt_list)))
