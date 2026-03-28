N, M = map(int,input().split())
array_a = []
array_b = []

for i in range(N):
    A, B = map(int,input().split())
    array_a.append(A)
    array_b.append(B)
    

for i in range(1,M+1):
    ans = array_b.count(i) - array_a.count(i)
    print(ans)