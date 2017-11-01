#importing files we have created

import classes

acc1 = classes.BankAccount(100, 'Katie')

print(acc1)

acc1.withdraw(50)

acc1.deposit(500)

acc1.withdraw(1000)

acc2 = classes.BankAccountSpecial(200, 'Chris')

acc2.withdraw(100)
acc2.withdraw(101)
acc2.deposit(100)
acc2.withdraw(100)
