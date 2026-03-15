def solve():
    H, W, Q = map(int,input().split())

    for _ in range (Q):
        query = list(map(int, input().split()))
        t = query[0]

        if t == 1:
            R = query[1]
            
            # ここを追加！：食べる数を計算する
            ans = R * W
            print(ans)

            H -= R

        elif t == 2:
            C = query[1]

            ans = H * C
            print(ans)

            W -= C

if __name__ == '__main__':
    solve()