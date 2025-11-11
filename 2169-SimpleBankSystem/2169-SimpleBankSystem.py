# Last updated: 11/11/2025, 1:55:27 AM
class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (0 <= account1 - 1 < len(self.bal)) or not (0 <= account2 - 1 < len(self.bal)):
            return False

        if self.bal[account1 - 1] < money:
            return False
        else:
            self.bal[account1-1] = self.bal[account1-1] - money
            self.bal[account2-1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if not (0 <= account - 1 < len(self.bal)):
            return False
        else:
            self.bal[account-1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (0 <= account - 1 < len(self.bal)) or self.bal[account-1] < money:
            return False
        else:
            self.bal[account-1] -= money
            return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)