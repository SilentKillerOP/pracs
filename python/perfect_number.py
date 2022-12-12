number = int(input("Enter the number:"))
def perfectnum(number):
    sum1 = 0
    for i in range(1,number):
        if(number%i==0):
            sum1+=i

    if(sum1==number):
        print(f"{number} is a Perfect Number")
    
    else:
        print(f"{number} is not a Perfect Number")

perfectnum(number)