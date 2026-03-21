#自力で解けたコード

#入力
N = int(input())
A = list(map(int,input().split()))

#並び替え
A.sort()

#判定処理
for i in range(1,N):
    #重複が見つかればbreak
    if A[i] == A[i-1]:
        print("No")
        break
#重複なければ成功
else:
    print("Yes")