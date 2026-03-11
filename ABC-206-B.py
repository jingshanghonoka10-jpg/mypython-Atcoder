N = int(input())

#初期値
i = 0
money = 0

#演算
while money < N:
    i += 1        #ここ順番注意！moneyとの順番を逆にしてしまうと
    money += i    #余計に(i+1)された計算結果になってしまう

print(i)