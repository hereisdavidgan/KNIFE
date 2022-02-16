# a = input()
# b = list(a[::-1])
# c = {}.fromkeys(b).keys()
# print(''.join(c))

# i = bin(int(input()))
# # i = str(bin(int(input())))
# print(i.count('1'))


i = input().split(';')
x = y = 0
for j in i:
    if 2 <= len(j) <= 3 and j[0] in 'AWSD' and j[1:].isdigit():
        k = int(j[1:])
        if j[0] == 'A':
            x -= k
        if j[0] == 'D':
            x += k
        if j[0] == 'S':
            y -= k
        if j[0] == 'W':
            y += k
print(f'{x},{y}')

