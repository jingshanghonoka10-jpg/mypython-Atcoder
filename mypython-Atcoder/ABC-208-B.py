#<自作コード>

#アルゴリズム考えるためにわざと関数使用で自分で階乗求めた
def upstars(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i
    
    return ans

#モジュールVer:

#import math
#coin = math.factorial(i) ←これで階乗求められる


def main():

    #入力
    P = int(input())
    count = 0

    for i in range(10,0,-1):
        coin = upstars(i)
        
        if P >= coin:       #　←実はif文なくてもPythonは成り立つらしい
            c = P // coin   #　←「//」には割る数より小さい場合は自動で0になる
            count += c      #　よってifがなくてもcに足されても0なので問題なし
            P %= coin
    
    print(count)

if __name__ == "__main__":
    main()
