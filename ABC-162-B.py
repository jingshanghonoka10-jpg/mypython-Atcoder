#自作コード(解きなおし)

N = int(input())
ans = 0

for i in range(1, N +1):
    if i % 3 != 0 and i % 5 != 0:
        ans += i
    
print(ans)

#問題文に条件分岐の結果が書いてあるが、実質必要なのは数字になる部分だけ
#なのでそれ以外を判定することは不要



#計算量O(1)のコード

def sum_n(n):
    #1~nまでの和の公式
    return n * (n+1) // 2

def main():
    N = int(input())

    #全体の和　‐　3の倍数 - 5の倍数　+ 15の倍数の和 ←集合の理論、ベン図で分かる
    ans = sum_n(N) - sum_n(3) - sum_n(5) - sum_n(15)

    print(ans)

if __name__ == "__main__":
    main()