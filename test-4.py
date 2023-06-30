from lib.transaction import Transaction

transaction = Transaction()

transaction.add_item('Ayam Goreng', 2, 20000)
transaction.add_item('Pasta Gigi', 3, 15000)
transaction.add_item('Mainan Mobil', 1, 200000)
transaction.add_item('Mi Instan', 5, 3000)


transaction.check_order() 
print("Total belanja yang harus dibayarkan adalah: Rp", transaction.item_total_price)