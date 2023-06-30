from lib.transaction import Transaction

transaction = Transaction()

transaction.add_item("Permen", 2, 2000)
print("Item List Sebelum Update")
print(transaction.item_list)

transaction.update_item_name("Permen", "Permen Mantab")
transaction.update_item_quantity("Permen Mantab", 10)
transaction.update_item_price("Permen Mantab", 2500)
print("Item List Sesudah Update")
print(transaction.item_list)