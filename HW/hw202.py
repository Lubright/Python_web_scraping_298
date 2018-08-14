
# coding: utf-8

# In[80]:


from datetime import datetime
from datetime import timezone
from datetime import timedelta
import sys


# In[104]:


def gen_datetime_obj(line):
    line_list = [e for e in line.split(' ') if e != '']
    dt_str = ' '.join(line_list[0:-1])
#     print(dt_str)
    offset = int(line_list[-1][2])
    if line_list[-1][0] == '-':
        offset = offset
    else:
        offset = -offset
#     print(offset)
    offset_timedelta = timedelta(hours=offset)
    dt = datetime.strptime(dt_str, '%a %d %b %Y %X')
    dt = dt.astimezone(timezone(offset=offset_timedelta))
    dt = datetime.combine(dt.date(), dt.time())

    return dt


# In[105]:


def show_diff_datetime(line):
    #     print(line,type(line))
    if ',' in line:
        line = line.split(',')[0]
        days = int(line.split(' ')[0])
#         print(line,'ago')
#         print(days)

        if 1 <= days <= 6:
            print(line, 'ago')
        else:
            week = days//7
            if week == 1:
                print(week, 'week', end=' ago')
            elif week > 1:
                print(week, 'weeks', end=' ago')

    else:
        line = line.split(':')
#         print(line)
        for i, e in enumerate(line):
            temp = int(e)
            if i == 0:
                if temp == 1:
                    print(temp, 'hour', end='')
                elif temp > 1:
                    print(temp, 'hours', end='')
                else:
                    continue
                break
            elif i == 1:
                if temp == 1:
                    print(temp, 'minute', end='')
                elif temp > 1:
                    print(temp, 'minutes', end='')
                else:
                    continue
                break
            elif i == 2:
                if temp == 1:
                    print(temp, 'second', end='')
                elif temp > 1:
                    print(temp, 'seconds', end='')
                break
        print(' ago')


# In[108]:

try:

    t0 = []
    t1 = []
    n = int(input())
    for i in range(n):
        line, line2 = input(), input()
        dt = gen_datetime_obj(line)
    #     print(dt)
        # line2 = input()
        dt2 = gen_datetime_obj(line2)
    #     print(dt2)
        # show_diff_datetime((dt2-dt).__str__())
        t0.append(dt)
        t1.append(dt2)
    #     print(dt2-dt)

    for i in range(len(t0)):
        show_diff_datetime((t1[i]-t0[i]).__str__())
except:
    sys.exit(1)
