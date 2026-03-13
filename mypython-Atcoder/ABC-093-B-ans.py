#入力
A, B ,K = map(int,input().split())

#リストの用意、この時点でsetを使って重複を防ぐ
ans = set()

#AからK番目以内の数をチェック
#min()を使用して,A+KがBより大きいときに無駄に処理しないように制限
for i in range (A, min(A + K, B + 1)):
    ans.add(i)


#BからK番目以内の数をチェック
#max()を使用して,B - K ＋ 1がAよりも小さいときに無駄に処理しないように制限
for i in range (max(B - K + 1, A), B + 1):
    ans.add(i)

#出力,この時にsortedを使って順番を整理しておく
for num in sorted(ans):
    print(num)