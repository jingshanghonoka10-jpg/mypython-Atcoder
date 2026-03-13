def count_pass(scores, P):

    count = 0
    for i in scores:
        if i >= P:
            count = count + 1
        
        else:
            continue

    return count

def main():
    N, X = map(int,input().split())
    scores_point = list(map(int,input().split()))

    ans = count_pass(scores_point, X)

    print(ans)

if __name__ == "__main__":
    main()
