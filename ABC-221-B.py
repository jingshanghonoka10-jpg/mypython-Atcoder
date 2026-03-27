S = input()
T = input()
n = len(S)

#最初の判定
if S == T:
    print('Yes')
    exit()

#文字列をリスト化しないと入れ替えが不可能
S_list = list(S)

for i in range(n-1):
    #リストの要素の入れ替え方
    S_list[i],S_list[i+1] = S_list[i+1],S_list[i]
    
    #文字列に戻して判定
    if "".join(S_list) == T:
        print('Yes')
        break
    
    #リストの要素をもとに戻して次へ
    S_list[i],S_list[i+1] = S_list[i+1],S_list[i]

else:
    print('No')
