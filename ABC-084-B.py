def jadge(A,B,S):
    if len(S) != A + B + 1:
        return  False  

    if S[A] != '-' :
        return  False
    
    first_part = S[:A]
    second_part = S[A+1:]

    if first_part.isdigit() and second_part.isdigit():
        return True
    else:
        return False
    

def main():
    A, B =  map(int,input().split())
    S = input()

    if jadge(A,B,S) == True:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()

