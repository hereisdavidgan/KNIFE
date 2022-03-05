d = {}

while True:
    try:
        s = input().split("\\")[-1].split(" ")
        print(s)
        s1 = "{} {}".format(s[0][-16:], s[1])
        print(s1)
        if s1 not in d:
            d[s1] = 1
        else:
            d[s1] += 1
    except:
        break

temp = list(d.items())[-9:]
for i in temp:
    res = "{} {}".format(i[0], i[1])
    print(res)

i = input()
print(i)
j = i.lower()
print(j)
k = ord(j)+1
print(k)
l = chr(k)
print(l)

i = input()
res = []
for j in i:
    if j.isdigit():
        res.append(j)
    elif j.isupper() and j!= 'Z':
        res.append(chr(ord(j.lower())+1))
    elif j == 'Z':
        res.append('a')
    else:
        if j in 'abc':
            res.append('2')
        if j in 'def':
            res.append('3')
        if j in 'ghi':
            res.append('4')
        if j in 'jkl':
            res.append('5')
        if j in 'mno':
            res.append('6')
        if j in 'pqrs':
            res.append('7')
        if j in 'tuv':
            res.append('8')
        if j in 'wxyz':
            res.append('9')
print(''.join(res))
