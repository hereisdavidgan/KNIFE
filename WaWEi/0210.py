# i = input().upper()
# j = input().upper()
# l = 0
# for k in i:
#     if j == k:
#         l += 1
# print(l)



data = []
while True:
    try:
        n = input()
        ta = []
        for i in range(int(n)):
            ta.append(int(input()))
        uniq = set(ta)
        for j in sorted(uniq):
            print(j)
    except (EOFError, KeyboardInterrupt):
        break





