def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = '1'
n = int(input("give a number:"))
for i in range(n):
    s = next_number(s)
    print(s)
            
