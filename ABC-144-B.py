N = int(input())
jadge = True

for i in range(1,10):
    for j in range(1,10):
        if i * j == N:
            print('Yes')
            jadge = False
            break

    if jadge == False:
        break
else:
    print('No')