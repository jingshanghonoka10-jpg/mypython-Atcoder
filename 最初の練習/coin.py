import math as m

P = int(input())
count = 0
for i in range(10, 0, -1):

    coin = m.factorial(i)

    count += P // coin
    P %= coin

print(count)

#もし関数使うなら
def upstairs(N):
    sum = 0
    for i in range(1, N+1):
        sum *= i
    return sum
