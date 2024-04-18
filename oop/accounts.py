import pytz
import datetime


class Account:
    """ Simple account class with balance """

    # Static method does not require the use of `self` in it 
    # and is shared among all object instances
    # the leading `_` means the method or attribute is for
    # internal use only
    # double `__` means it is a protected method or attribute
    # and cannot be modified outside the class as python mangles it
    @staticmethod
    def _current_time():
        """ returns aware utc time """
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # use Account._current_time as the static method is in the 
            # Account class declaration and not in the instance namespace. 
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()

    steph = Account("steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()