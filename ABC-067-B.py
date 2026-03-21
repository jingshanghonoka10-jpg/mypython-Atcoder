#自力で解けたコード

#入力
N, K = map(int,input().split())
l = list(map(int,input().split()))

#並び替え＆初期値設定
l.sort(reverse=True)
ans = 0

#大きいものをKの範囲まで処理
for i in range(K):
    ans += l[i]

#出力
print(ans)