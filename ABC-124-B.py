N = int(input())
H = list(map(int,input().split()))

max = 0
count = 0
for i in range(N):

    if H[i] >= max:
        count += 1
        max = H[i]

print(count)