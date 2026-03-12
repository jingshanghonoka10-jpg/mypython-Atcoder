#自力で解ききれたコード

#入力
A, B = map(int,input().split())

#演算,iの範囲はA,Bの範囲が100までなのでそこから求める
for i in range (1,10001):

    a = i * 8 // 100
    b = i * 1 // 10
    
    #税率が一致したiが答え
    if A == a and B == b:
        print(i)
        break
    
    #2重ループでなかった時を対処した（下に別解あり）
    else:
        if i == 10000:
            print(-1)
            break

        

#Pythonはforのループの最後に字下げ（インデント）でelseをくっつけることができる
for i in range (1,10001):

    a = i * 8 // 100
    b = i * 1 // 10
    
    if A == a and B == b:
        print(i)
        break
    
#これだけでおしまい、字下げするとループの中で探しきれなかった場合として実行される
else:
    print(-1)