#自作コード（間違ってるコード）

#入力
N = int(input())
A = list(map(int,input().split()))

#初期値設定
count = 0

#要素のチェック
for i in range(N):
    
    if A[i] % 2 == 0:
        a = A[i]     #　←ここなんかエラーが立て続いたためこうなった
        a //= 2      #  最終的に A[i] = A[i] // 2　で動いた
        A[i] = a 
        i += 1
    else:
        count = 0
        break
    
    #ここでカウントをすることは要素が割れた数だけカウントしていることに気が付かなかった
    count += 1

print(count)