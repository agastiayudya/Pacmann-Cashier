from lib.transaction import Transaction

transaction = Transaction()

transaction.add_item('Ayam Goreng', 2, 20000)
transaction.add_item('Pasta Gigi', 1, 15000)

transaction.delete_item('Pasta Gigi')

transaction.check_order() 