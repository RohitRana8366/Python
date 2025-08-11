'''create account with 2 attributes- balance and account numbers create methods for debit credit and printing the balance with the help of 
encapssualtion'''
class account:
    #paramitrized constructor
    def __init__(self, balance, account_no):
        self.balance=balance
        self.account_no=account_no
    
    #debit account
    def debit(self, amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balace())


    #credit ammount
    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"was credited")
        print("total balance=",self.get_balace())

    #get balance
    def get_balace(self):
        return self. balance
    
    #print to account details
    def print_account_details(self):
        print("Account Number:",self.account_no)
        print("Current Balance: Rs.",self.balance)

 #final calling       
account1=account(10000,12345)
account1.print_account_details()
account1.debit(1000)
account1.credit(500)




        