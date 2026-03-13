#N進法から10進法への変換関数
def ary_system(num,n):

    ans = 0
    i = 0
    
    #1桁ずつ取り出して計算
    while num > 0:
        ans += (num % 10) * n**i
        num = num // 10
        i += 1         #　←　+=　を反転して書いてしまった,解けなかった原因

    return ans 

def main():
    #入力
    K = int(input())
    A, B = map(int,input().split())
    
    #出力
    print(ary_system(A, K) * ary_system(B ,K))

if __name__ == "__main__":
    main()
