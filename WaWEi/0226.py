# i = input().split('.')
# iiii = ''
# for ii in i:
#     iii = bin(int(ii))
#     iiii += iii
# print(iiii)

# n = 5
# number = 15
# L = []
# for i1 in range(n):
#     L.append([])
#
# while number > 0:
#     for i2 in range(n):
#         L[i2].append(str(number - i2))
#     number -= n
#     n -= 1
# print(L)

i = int(input())
iii = [i]
iiii = [0]
for ii in range(5):
    iii.append(iii[ii]/2)
    iiii.append(iiii[ii]+2*iii[ii])
print(iiii)
print(iii)




