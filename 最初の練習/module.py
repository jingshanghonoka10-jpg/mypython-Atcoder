import random as r

N = int(input())

clothes = []

for i in range(N):
    s = input()
    clothes.append(s)
    
print(r.choice(clothes))