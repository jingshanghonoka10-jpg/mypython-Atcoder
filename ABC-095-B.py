N, X = map(int, input().split())
m_list = [int(input()) for _ in range(N)]

X -= sum(m_list)
counter = N
m = min(m_list)

while X >= m:
    counter += 1
    X -= m

# for文の部分は　counter += X // m　でも可
    
print(counter)