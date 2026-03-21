#自力で解けた

#入力
N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))

#初期値設定(最初の数値は入れておく)
B = T - H[0] * 0.006
n = 1

for i in range(1,N):
    #平均気温計算
    a = T - H[i] * 0.006

    #平均値からの差の絶対値の比較
    if abs(A - a) < abs(A - B):
        n = i + 1
        B = a
#出力
print(n)