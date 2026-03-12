#入力
N, K = map(int,input().split())

#繰り返し処理
for i in range(K):
    
    #条件分岐
    if N % 200 == 0:
        N = N // 200
    else:
        N =(N*1000) + 200  #自力で考えられた！
        #N = int(str(N) + "200")　←　文字列に変換して計算するやつ,処理が若干遅い

#出力
print(N)