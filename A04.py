N = int(input())
A = [0,0,0,0,0,0,0,0,0,0]
i = 0

while N > 0:
    A[9-i] = N % 2
    N //= 2
    i += 1

num = "".join(map(str,A))
print(num)