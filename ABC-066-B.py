S = input()

S = S[:-1]

while len(S) > 0:
    n = len(S)

    if n % 2 == 0:
        half = n // 2

        if S[:half] == S[half:]:
            print(n)
            break
    
    S = S[:-1]