#入力＆初期値
a, b = map(int,input().split())
num = []

#辞書で小さいほうを決めてから配列に数字を入れていく
if a <= b:
    for i in range(b):
        num.append(a)

else:
    for i in range(a):
        num.append(b)

#配列なので数字にしてく
ans = int(''.join(map(str,num)))

print(ans)