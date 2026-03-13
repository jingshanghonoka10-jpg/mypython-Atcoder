#攻撃等に関しては割り算で切り上げするテクニックを使用する

# (HP + 攻撃力 - 1) // 攻撃力

A, B, C, D = map(int,input().split())

if (C + B - 1) // B  <=  (A + D - 1) // D:
    print("Yes")
else:
    print("No")