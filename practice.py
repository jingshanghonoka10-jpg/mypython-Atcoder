#自作コード
#8進法から9進法への変換関数(10進数経由)
def ary_system(num):

    #下記の条件分岐では num == 0 の時の場合を書いていないから先に書く
    if num == 0:
        return "0"     #　←ここでの0を数字で返しちゃうとstrとintの間で喧嘩が起こる（41行目）
    
    #初期値設定
    a = 0
    i = 0

    #1桁ずつ取り出して10進数へ変換
    while num > 0:
        a += (num % 10) * 8**i   #aに10進法の数字を入れる
        num = num // 10
        i += 1    
    

    #10進数から9進数へ
    
    #リストに%の計算した結果を入れていく作戦
    b = []
    
    #余りの計算で9進数を作る
    while a > 0 :
        b.append(a % 9)
        a = a // 9
    
    #出力の順番が逆なので反転させる
    b.reverse()

    #リストの中身を結合
    ans = "".join(map(str,b))

    return ans


def main():

    #入力
    N, K = map(int,input().split())
    
    #K回繰り返す
    while K > 0:
        num = ary_system(N)
        
        #8→5に変化させるコード
        num = num.replace("8", "5")

        #繰り返しをするのにint型に戻さないと摩擦が起こる
        N = int(num)
        K -= 1
    
    print(N)


if __name__ == "__main__":
    main()





#Geminiの模範解答

# 10進数から9進数の文字列に変換する関数

def base10_to_base9(num):
    if num == 0:
        return "0"
    
    res = ""
    while num > 0:
        # 余りを文字列にして、前へ前へとくっつけていく（反転の手間が省ける！）
        res = str(num % 9) + res
        num //= 9
        
    return res

def main():
    # Nは文字列のまま、Kは整数として受け取る
    N, K = input().split()
    K = int(K)
    
    for _ in range(K):
        #  int(文字列, 8) で、8進数から10進数へ一発変換が可能
        num_10 = int(N, 8)
        
        # 10進数から9進数の文字列に変換
        num_9_str = base10_to_base9(num_10)
        
        # "8" を "5" に置き換えて、次のループのNにする
        N = num_9_str.replace("8", "5")

    print(N)

if __name__ == "__main__":
    main()