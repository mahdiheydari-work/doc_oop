class bank:

    def __init__(self,name):
        self.name = name 
        self.amount = 0
        print("accont created, owner: ",self.name)

    def deposit(self,amount):
        if amount > 0:
            self.amount += amount
            print("deposit done")
        else:
            print("eror: amount is not enoght")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.amount:
                self.amount -= amount
                print("withdraw ok")
        else:
            print("eror: amount is not enoght")

    def get_amount(self):
        return "your balace is " + str(self.amount )



acc_1 = bank("mahdi")
acc_1.deposit(1500)
acc_1.deposit(1500)
acc_1.deposit(1500)
print(acc_1.get_amount())
acc_1.withdraw(4000)
print(acc_1.get_amount())