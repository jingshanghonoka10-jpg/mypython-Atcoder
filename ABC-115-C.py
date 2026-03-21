#入力＆初期配列設定
N, K = map(int,input().split())
tree = []

#配列に要素を追加していく
for i in range(N):
    h = int(input())
    tree.append(h)

#最大、最小を探すのに並び替えたほうが考えやすいと思った
tree.sort()

#-------ここからが自力で解けなかったところ--------

#初期値設定、ここで0にしてしまうと一生0で差が求められないから無限大を使用する
ans = float('inf')

#　N-K＋1　でNのうちK個選ぶという時のスライドが可能になる
for i in range(N-K+1):
    
    # i+k-1番目はK個抜き出す中の最大、iは最小値
    diff = tree[i + K - 1] - tree[i]

    if diff < ans:
        ans = diff

print(ans)