#自作コード
#今回はA, Bの範囲が莫大のため、計算量がオーバーする→不正解
A, B ,K = map(int,input().split())
ans = []

for i in range(A, B+1):

    if i < A + K :
        ans.append(i)
    elif i > B - K:
        ans.append(i)
        
        
ans = sorted(set(ans))

for ans in ans:
    print(ans)