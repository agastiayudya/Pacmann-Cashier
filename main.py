from lib.transaction import Transaction

transaction = Transaction()

transaction.add_item("Permen", 2, 2000)
transaction.add_item("Coklat", 1, 15000)
print("Item List Sebelum Update")
print(transaction.item_list)

transaction.update_item_name("Permen", "Permen Mantab")
transaction.update_item_quantity("Permen Mantab", 10)
transaction.update_item_price("Permen Mantab", 2500)
print("Item List Sesudah Update")
print(transaction.item_list) 

transaction.delete_item("Coklat")
print("Item List Sesudah Penghapusan Item")
print(transaction.item_list) 

transaction.reset_transaction() 
print("Item List Sesudah Reset")
print(transaction.item_list) 

transaction.add_item("Permen", 2, 2000)
transaction.add_item("Coklat", 1, 15000)
transaction.add_item("Lolipop", 10, 20000)
print("Item List Check Order")
transaction.check_order()