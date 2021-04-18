class Budget:

    def __init__(self, food, clothing, entertain):

        self.food = food
        self.clothing = clothing
        self.entertain = entertain


    def compute_balances(self):
    
        print(f" The balance for food category is {self.food}")

        print(f" The balance for clothing category is {self.clothing}")

        print(f" The balance for entertainment category is {self.entertain}")



    def deposit_funds(self, foodDeposit, clothingDeposit, entertainDeposit):

        print("----Depositing funds into the categories----\n")

        self.food = self.food + foodDeposit
        self.clothing = self.clothing + clothingDeposit
        self.entertain = self.entertain + entertainDeposit

        print("Category Balance after deposits:\n")

        self.compute_balances()


    def withdraw_funds(self, foodWithdraw, clothingWithdraw, entertainWithdraw):

        print("----Withdrawing funds from categories----\n")


        self.food = self.food - foodWithdraw
        self.clothing = self.clothing - clothingWithdraw
        self.entertain = self.entertain - entertainWithdraw

        print("Category Balance after withdrawals:\n")

        self.compute_balances()

    
    








