#自分で思いつくコード（str型に変換してから見る）
A, B = map(int,input().split())

count = 0  # ← ループの中に入れてずっと答えが０というミスをしてしまった

for i in range (A, B+1):

    #int型→str型へ変換しリストとして桁を扱えるように
    i = str(i)
    
    #条件判定（str型なのでリストで比べる）
    if i[0] == i[4]:
        if i[1] == i[3]:
            count += 1
    
print(count)


#計算でそのままint型として扱う
A, B = map(int,input().split())

count = 0

for i in range (A, B+1):
    
    #分かりやすくするためにそれぞれの計算を変数に代入
    a = i % 10            #1桁目
    b = (i // 10) % 10    #2桁目
    c = (i // 1000) % 10  #4桁目
    d = i // 10000        #5桁目
    
    #条件判定
    if a == d:
        if b == c:
            count += 1
    
print(count)