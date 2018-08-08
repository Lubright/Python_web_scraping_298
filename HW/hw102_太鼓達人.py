score = 0
combo = 0
list_combo_cnt = []
temp_cnt = 0

line1 = input()
line2 = input()

check_len = min([len(line1), len(line2), 100])

for i in range(check_len):
    if line1[i] == line2[i]:
        if line1[i] == 'R' or line1[i] == 'B':
            temp_cnt += 1
            score += (temp_cnt*100)
    else:
        list_combo_cnt.append(temp_cnt)
        temp_cnt = 0
list_combo_cnt.append(temp_cnt)

print(score, max(list_combo_cnt))
