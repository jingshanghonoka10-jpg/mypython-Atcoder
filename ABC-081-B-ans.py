#入力
N = int(input())
A = list(map(int,input().split()))

#初期値設定
count = 0


while True:
    #リストの要素が2で割れるか確認
    for i in range(N):

        if A[i] % 2 == 0:
            jadge = True
        else:
            #奇数があったらFalse代入してfor文からbreak
            jadge = False
            break
    
    #奇数があった時while文からbreka(自動的にcountはwhile文を回す前の0になる)
    if jadge == False:
        break
    
    #ここまでたどり着くのは要素すべてが偶数だったときのみ
    #要素をすべて2で割る作業
    for i in range(N):
        A[i] = A[i] // 2
    
    #回数を1プラスする
    count += 1

print(count)



#Pythonのリストの便利機能
#リストの中の全ての要素の条件を判定する
# all( 条件式 for 変数 in リスト )

#別解(Geminiより)
N = int(input())
A = list(map(int, input().split()))

count = 0

# Aの中身(a)が「すべて」偶数である間、ループを続ける
while all(a % 2 == 0 for a in A):
    # リストの内包表記で、全員を2で割った新しいリストに上書きする
    A = [a // 2 for a in A]
    count += 1

print(count)


#別解(公式)

# 何回2で割れるかを数える関数（リストの要素に適応）
# 奇数がある時は自動的に0になる
# 途中まで偶数で途中から奇数になった時もそこでストップする
def how_many_times_divisible(n):
    ans = 0
    while n % 2 == 0:
        n //= 2  
        ans += 1
    return ans

# 入力
N = int(input())
A = list(map(int, input().split()))

# リストAに関数を適応してansの最小値が答え
ans = min(map(how_many_times_divisible, A))

# 出力
print(ans)