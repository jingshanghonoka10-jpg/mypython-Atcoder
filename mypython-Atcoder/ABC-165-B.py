#入力
X = int(input())

#初期値設定
money = 100
ans = 0

#演算
while money < X:
    money += money // 100   #ここの計算をint(money * 0.01)でやったら誤差で数値が変化する
    ans += 1                #最初からint型で数字を扱えるように考えるようにする
#出力
print(ans)