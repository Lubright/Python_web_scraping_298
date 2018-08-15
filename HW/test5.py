from collections import deque
prefix = ['(', '[', '{', '<']
postfix = [')', ']', '}', '>']
map_table = {')': '(', ']': '[', '}': '{', '>': '<'}
unmatch_list = deque()
match_list = deque()


def checkValid(line):
    temp_list = line[:]
    cnt1 = 0
    cnt2 = 0
    check_found = True
    for c in temp_list:
        cnt1 += 1
        if c in prefix:
            unmatch_list.append([cnt1, c])
        elif c in postfix:
            del_index = None
            check_found = False
            if len(unmatch_list) > 0:
                temp = unmatch_list.pop()
            else:
                return False
            if map_table[c] == temp[1]:
                check_found = True
                temp.extend([cnt1, c])
                match_list.append(temp[:])
            else:
                check_found = False
                unmatch_list.append(temp)
                return False
            # for i, temp in enumerate(unmatch_list):
            #     if map_table[c] == temp[1]:
            #         check_found = True
            #         # del_index=i
            #         temp.extend([cnt1, c])
            #         match_list.append(temp[:])
            #         del unmatch_list[i]
            #         break
            #     else:
            #         check_found = False
        else:
            # check_found = False
            pass

    # print('unmatch_list:', unmatch_list)
    # print('match_list:', match_list)

    if len(unmatch_list) > 0:
        return False

    if check_found:
        return True
    else:
        return False


numOfData = int(input())

if numOfData <= 10000:
    test_data = []

    for i in range(numOfData):
        line = input()
        if len(line) <= 1024:
            test_data.append(line)
        else:
            print('N')
            continue
    for e in test_data:
        # print(e)
        match_list.clear()
        unmatch_list.clear()
        result = checkValid(e)
        if result:
            print('Y')
        else:
            print('N')

else:
    print('N')
