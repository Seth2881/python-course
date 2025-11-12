class BankAccount :
    def __init__(self,name:str='John',balance:int=1000) :
        self.name = name
        self.balance = balance

    def deposit(self,amount) :
        if amount > 0 :
            self.balance += amount
        else :
            print('transaction aborpted : cannot deposity a negative amount of money')

    def withdraw(self,amount) :
        if self.balance - amount >=0 :
            self.balance -= amount
        else :
            print('transaction aborpted : you can\'t have negative amount of money')

    def display(self) :
        print(f'Name : {self.name.upper()} | Balance : {self.balance}$')

##################################################################

def test_bank_account():
    print("=== CRÉATION DES COMPTES ===")
    catherine = BankAccount('Catherine', 300000)
    john = BankAccount('SpongeBob',1)
    catherine.display()
    john.display()

    # 1 Test dépôt
    print("\n=== TEST DÉPÔT ===")
    catherine.deposit(5000)
    catherine.display()  # devrait afficher 305000
    john.deposit(-50)    # dépôt négatif → transaction refusée

    # 2 Test retrait
    print("\n=== TEST RETRAIT ===")
    catherine.withdraw(10000)
    catherine.display()  # 295000
    john.withdraw(1500)  # solde insuffisant → transaction refusée
    john.display()

    # 3 Test dépôt + retrait successifs
    print("\n=== TEST COMBINÉ ===")
    john.deposit(250)
    john.withdraw(100)
    john.display()

    # 4 Test de gros retrait (égal au solde)
    print("\n=== TEST RETRAIT EXACT ===")
    john.withdraw(john.balance)
    john.display()  # solde = 0

# --- Lancer le test ---
if __name__ == "__main__":
    test_bank_account()