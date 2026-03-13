def check_bodget(prices,X):

    total = sum(prices)
    if total <= X:
        return "Yes"
    else:
        return "No"


def main():
    #入力
    N,X = map(int,input().split())
    snaks_list = list(map(int,input().split()))

    #関数呼び出し
    ans = check_bodget(snaks_list,X)

    print(ans)

if __name__ == "__main__":
    main()
