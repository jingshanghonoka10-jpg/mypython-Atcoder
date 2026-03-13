#入力
A, B ,C , D = map(int,input().split())

#演算
if (A + D - 1) // D >= (C + B - 1) // B:
    print("Yes")
else:
    print("No")

#(A + D - 1) // D　←　余りが出たときにそのあまりも＋１して処理するよって時の公式
#例；ケーキの箱詰め　4個のケーキが入る箱　と　ケーキ11個　→　必要な箱の数3個（2箱ピッタリ,1箱あまり用）
#攻撃もその理論

#別解（繰り返し）

A, B, C, D = map(int, input().split())

while True:
    # まず高橋君が攻撃
    C -= B
    if C <= 0:
        print("Yes")
        break  # 勝負がついたらループを抜ける
    
    # 次に青木君が攻撃
    A -= D
    if A <= 0:
        print("No")
        break