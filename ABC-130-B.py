N, X = map(int,input().split())
L = list(map(int,input().split()))

counter = 1
distance = 0
for i in range(N):
    distance += L[i]

    if distance <= X:
        counter += 1

    else:
        break

print(counter)