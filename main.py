from lib.transaction import Transaction

transaction = Transaction()

transaction.add_item("Permen", 2, 2000)
print(transaction.item_list)