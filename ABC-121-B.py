#入力&初期値設定
N, M = map(int,input().split())
drink = []
for i in range (N):
    A, B = map(int,input().split())
    drink.append([A,B])

#価格で配列の並び替え
drink.sort()
total_cost = 0

for i in range(N):
    #価格とストックを分かりやすく代入
    price = drink[i][0]
    stock = drink[i][1]

    #ストックがMに達していなかったら価格にそれまでの数を掛け算し、M-ストックの計算する
    if M >= stock:
        total_cost += price * stock
        M -= stock
    
    #ストックがMに達したら価格×Mして終了
    else:
        total_cost += price * M
        break

print(total_cost)