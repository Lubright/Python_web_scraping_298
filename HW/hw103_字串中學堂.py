word_map = {}
while True:
    line = input()
    if line == '0':
        break
    temp = [e for e in line.split(' ') if e != '']
    # print(temp)
    word_map[temp[1]] = temp[0]

keys_sorted = sorted(word_map.keys())
# print(keys_sorted)

cnt1 = 0
for e in keys_sorted:
    cnt1 += 1
    if cnt1 == len(keys_sorted):
        print(word_map[e], end='.')
    else:
        print(word_map[e], end=' ')
