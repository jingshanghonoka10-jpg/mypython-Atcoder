#解けるけどTLE
Q = int(input())
#ans_set = {}
ans_array = []
ans = []

for i in range(Q):
    A, B = map(int,input().split())

    if A == 1:
        #ans_set.add(B)
        ans_array.append(B)
    
    else:
        #even_set = [j for j in ans_array if j < B]
        #ans_set = set(even_set)
        #ans_set = list(ans_set)
        ans_array = [j for j in ans_array if j > B]

    #ans_array.append(len(ans_set))
    ans.append(len(ans_array))

for i in range(len(ans)):
    print(ans[i])
