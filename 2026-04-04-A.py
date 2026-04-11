##自分で書いたコード（CA）
import sys

M, D = map(int,input().split())
num_list = [3,5,7,9]
count = 0

if M == 1 and D == 7:
    print('Yes')
    sys.exit()
    

for i in range(len(num_list)):
    if M == D == num_list[i]:
        print('Yes')
        break

else:
    print('No')

##模範解答
m, d = map(int, input().split())

gossekulist = [(1,7), (3,3), (5,5), (7,7), (9,9)]

if ((m,d) in gossekulist):
	print("Yes")
else:
	print("No")
