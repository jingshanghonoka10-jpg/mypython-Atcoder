#自作コード
X, T = map(int,input().split())
A = list(map(int,input().split()))

value = A[0]
print(0, A[0])

for i in range(1, X+1):
    if T <= abs(value - A[i]):
        print(i, A[i])
        value = A[i]

#解説コードも同じ方法だった
