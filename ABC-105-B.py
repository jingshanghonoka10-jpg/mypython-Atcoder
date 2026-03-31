N = int(input())
a = N // 4
b = N // 7
jadge = True

for i in range(0,a+1):
    for j in range(0,b+1):
        if 4 * i + 7 * j == N:
            print('Yes')
            jadge = False
            break
    
    if jadge == False:
        break
else:
    print('No')
