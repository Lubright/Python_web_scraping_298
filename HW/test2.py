from collections import OrderedDict
from collections import defaultdict

dict1 = OrderedDict()
sub_dict1 = {}
animal_seq = []
site_seq = []
check = True
while True:
    try:
        line = input()
        temp_list = [e for e in line.split(' ') if e != '']

        dict1.setdefault(temp_list[2], {})
        if 0 < int(temp_list[1]) <= 100:
            sub_dict1[temp_list[0]] = int(temp_list[1])
        else:
            continue
        if temp_list[0] not in dict1[temp_list[2]]:
            dict1[temp_list[2]].update(sub_dict1.copy())
        else:
            dict1[temp_list[2]][temp_list[0]] += sub_dict1[temp_list[0]]
        sub_dict1.clear()

    except EOFError as e:
        break
    except:
        check = False
        break

if check:
    dict2 = defaultdict(list)
    dict3 = OrderedDict()
    for k, v in dict1.items():
        for k2, v2 in v.items():
            dict2[v2].append(k2)
        dict3.setdefault(k, dict2.copy())

        dict2.clear()
    # print(dict3)
    for k, v in dict3.items():
        print('{}:'.format(k), end='')
        temp_len = len(v)
        cnt1 = 0
        for k2 in sorted(v, reverse=True):
            cnt2 = 0
            temp_len2 = len(v[k2])
            cnt1 += 1
            if cnt1 == temp_len:
                for e in v[k2]:
                    cnt2 += 1
                    if cnt2 == temp_len2:
                        print('{} {}'.format(e, k2))
                    else:
                        print('{} {}'.format(e, k2), end=',')
            else:
                for e in v[k2]:
                    print('{} {}'.format(e, k2), end=',')
