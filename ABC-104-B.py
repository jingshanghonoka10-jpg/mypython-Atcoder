S = input()
jadge = True

if S[0] != 'A':
    jadge = False
   
if S[2:-1].count('C') != 1:
    jadge = False
    
if sum(map(str.isupper, S))!= 2:
    jadge = False
    

if jadge  == True:
    print("AC")

else:
    print("WA")
