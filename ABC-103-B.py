#入力＆初期値設定
S = input()
T = input()
n = len(S)

for i in range(n):
    #判定
    if S == T :
        print('Yes')
        break

    #文字ずらし
    a = S[:-1]
    b = S[-1]
    S = b + a

else:
    print('No')
    