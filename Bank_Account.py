class BankAccount:
    def __init__(self,acc_holder_name,acc_no,balance=0):
        self.acc_holder_name=acc_holder_name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self):
        amount=float(input("Enter the Deposit Amount : "))
        self.balance+=amount
        print("The Total amount present in your account after deposit is : ",self.balance)
    def withdrawal(self):
        amount=float(input("Enter the Withdrawal Amount : "))
        if amount>self.balance:
            print("Insuffient Funds!!")
        else:
            self.balance-=amount
            print("The Total amount present in your account after withdrawal is :  ",self.balance)
    def display(self):
        print("The Total amount present in your account :",self.balance)
def detail():
    acc_holder_name=input("Enter the account holder name:").upper()
    acc_no=int(input("Enter the account number:"))  
    print(acc_holder_name+" YOUR ACCOUNT SUCCESSFULLY CREATED!!")
    acc=BankAccount(acc_holder_name,acc_no) 
    while(True):
        choice=int(input("Enter a number(1:Deposit,2:Withdraw or 3:Display):"))
        if choice==1:
            acc.deposit()
        elif choice==2:
            acc.withdrawal()  
        elif choice==3:
            acc.display()
        else:
            break
if __name__=='__main__':
    detail()
