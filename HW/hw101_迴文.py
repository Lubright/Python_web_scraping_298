
result = []


def isPalindrome(s1):
    return s1 == s1[::-1]


while True:
    line = input()
    if line == '-----':
        break
    if isPalindrome(line):
        result.append('YES')
    else:
        result.append('NO')

for e in result:
    print(e)
