#入力
D,S = map(int,input().split())

#カロリー計算関数
def calc_total_calories(D,S):
    A = D + S
    return A

#出力
print(calc_total_calories(D,S))