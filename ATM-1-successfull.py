
global b
b=20000
def home():
    print('\r')
    print("-"*80)
    print("                            WELCOME TO 'ATM'   ")
    print("-"*80)
    print('\r')
    print(" PRESS 1 TO CHECK BALANCE ->")
    print('\r')
    print(" PRESS 2 TO DEPOSIT AMOUNT ->")
    print('\r')
    print(" PRESS 3 TO ASK FOR LOAN ->")
    print('\r')
    print(" PRESS 4 TO WITHDRAW AMOUNT ->")
    print('\r')
    
def balance():
    global b
    return(b)
    
def deposit(amt):
    global b
    b=(b+amt)
    print("You have successfully deposited = Rs. '",amt,"' in your account.")
    return(b)
    home()
    
def loan_lelo(amt):
    global b
    if (amt <= 1/2(b)):
        print("Successful ur loan has been granted")
        b = (b+amt)
        print(b)
        return(b)
        home()
    else:
        print("Increase your balance ,loan cannot be granted")
        home()     

def withdraw(amt):
    global b
    if(amt<=b):
       b=(b-amt)
       print("You have withdrawn '",amt,"' from your account.")
       return(b)
       
       home()

home()
while True:
    a=int(input("Enter your choice ->"))
    if(a==1):
       print(balance())
    elif(a==2):
       c=int(input("Enter the amount you want to deposit ->"))
       d=deposit(c)
       print(b)
    elif(a=3):
        c=int(input("Enter the loan amount that you want ->"))
        d=loan(c)   
        print(balance())
    elif(a==4):
       e=int(input("Enter the amt you want to withdraw ->"))
       withdraw(e)
       a=input("Do you want to check your total balance ->.(y/n)")
       if(a=='y'):
           print(balance())
           home()
       else:
           c=input("Do you want to check more. ->(y/n)")
           if(c=='y'):
               home()
           else:
               break
    else:
        break


   
#WORKING CODE
