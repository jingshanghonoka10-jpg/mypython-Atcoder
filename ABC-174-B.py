import math 
N, D = map(int,input().split())

ans = 0

for i in range(N):
    X, Y = map(int,input().split())

    result = math.sqrt(X*X + Y*Y)
    if result <= D:
        ans += 1

print(ans)