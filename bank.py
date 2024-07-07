'''  
make bank system that do :
    - show user details[name, age, address]
    - deposite money 
    - withdraw money
    - show user details with balance 

'''


class User():
    def __init__(self ,name ,age , address):
        self.name =name
        self.age =age
        self.address =address

    def user_detals(self):
        print(f"your name is:{self.name} \nyour age is:{self.age} \nyour address is: {self.address}" )

class Bank (User):
    def __init__(self ,name ,age , address):
        super().__init__(name ,age , address)
        self.balance =0 
    
    def deposite(self , money):
        self.balance += money
        print(f"you depositd: {money}")

    def withdraw(self , money):
        if money > self.balance:
            print("you are poor ")
            return
            
        self.balance -= money
        print(f"you withdrawed {money}")

    def show_details(self):
        self.user_detals()
        print(f"yor balance is {self.balance}")


# user=Bank("ahmed", 25 ,"ngeer")
# print(user.deposite(100000000))
# print(user.withdraw(100))
# print(user.withdraw(21000000000))
# print(user.show_details())





'''
-show user details[name, age, address]
    - deposite money 
    - withdraw money
    - show user details with balance

 '''


class User():
    def __init__(self ,name ,age ,address):
        self.name= name
        self.age= age
        self.address= address

    def show_user_details(self):
        print(f"your name is:{self.name} \nyour age is:{self.age} \nand your address:{self.address}")

class Bank(User):
    def __init__(self,name ,age ,address):
        super().__init__(name ,age ,address)
        self.balance=0

    def deposite(self ,money):
        self.balance += money
        print(f"you deposit:{money}\n your balance:{self.balance}")

    def withdraw(self, money):
        if money > self.balance :
            print("your money is not enough")
            return
        self.balance -= money 
        print(f"your withdraw :{money}\n your balance:{self.balance}")

    def show_details(self):
        self.show_user_details()
        print(f"your balance is:{self.balance}")







user=Bank("ahmed" ,25,"negeer")
print(user.deposite(2000))
print(user.withdraw(700))
print(user.withdraw(70000))
print(user.show_details())
