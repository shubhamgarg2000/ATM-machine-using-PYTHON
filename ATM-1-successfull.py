import hashlib

global b
b=20000
def home():
    flag = 0
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
    
    print(" PRESS 5 TO ADMIN ACCOUNT ->")
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
    
def admin_pass():
    print("Are you really admin? Then tell me the password")
    strr = input("Enter your secret password")
    
    print("We have added salt to password, so do not try to bruteforce it; haha i still know a implementation fault in it, can you find it and be admin")
    
    import hashlib, uuid
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(strr + salt).hexdigest()
    if result == "f6071725e7ddeb434fb6b32b8ec4a2b14dd7db0d785347b2fb48f9975126178f":
        flag = 1
        print("WOW! You have become admin")
        
    else:
        flag = 0
        
    
    
    
    
    
    
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
        
    elif(a=5):
        flag = 0
        admin_pass()
        home()
        
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
