def main():
    # 入力
    s = input()
    t = input()
    
    # Sは昇順（a, b, c...）に並び替えてくっつける
    S = "".join(sorted(s))
    
    # Tは降順（z, y, x...）に並び替えてくっつける ←これがわかっていなかった
    T = "".join(sorted(t, reverse=True))
    
    if S < T:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()