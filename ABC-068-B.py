#自作コード

#割った回数を求める関数
def count(num):
    c = 0
    while num % 2 == 0:
        c += 1
        num = num // 2   #　←num // 2　と書いてしまっていた。
                         #　 更新することを忘れずに
    return c

def main():
    #入力
    N = int(input())

    #初期値設定
    max_num = 0
    a = 0
    ans = 0

    #ループ処理
    for i in range (1, N+1):
        a = count(i)
        #割った回数の比較し、条件満たせば更新
        if a >= max_num:
            max_num = a
            ans = i
    
    #出力
    print(ans)

if __name__ == "__main__":
    main()


#公式の解法
# N <= 100までは決まっているので2でk回かけた数でN以下で大きいものを出力する

N = int(input())

#2で割り切れる累乗の100以下までをリストに入れる
powers = [1, 2,4, 8, 16, 32, 64]

ans = 1
#条件分岐　powersをN以下で回していき、最終的にN以下の最大値を出力
for i in powers:
    if i <= N:
        ans = i

print(ans)