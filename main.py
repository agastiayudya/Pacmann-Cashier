from lib.transaction import Transaction

def add_item_menu(transaction: Transaction):
    item_name = str(input("Masukkan nama item: "))
    quantity = int(input("Masukkan kuantitas item: "))
    price = int(input("Masukkan harga item: "))
    transaction.add_item(item_name, quantity, price)
    
def delete_item_menu(transaction: Transaction):
    item_name = str(input("Masukkan nama item: "))
    transaction.delete_item(item_name)

def reset_menu(transaction: Transaction):
    transaction.reset_transaction()
    
def update_pemesanan_menu(transaction: Transaction):
    try:
        print("1. Update Nama")
        print("2. Update Kuantitas")    
        print("3. Update Harga")
        
        selected_update_menu = int(input("Pilihan Menu: "))
        item_name = input("Nama Item yang akan Diupdate: ")
        
        if(selected_update_menu == 1):
            updated_field = str(input("Nama Baru: "))
            transaction.update_item_name(item_name, updated_field)          
        elif(selected_update_menu == 2):
            updated_field = int(input("Kuantitas Baru: "))
            transaction.update_item_quantity(item_name, updated_field) 
        elif(selected_update_menu == 3):
            updated_field = float(input("Harga Baru: "))
            transaction.update_item_price(item_name, updated_field)
    
    except:
        print("Input Invalid")              
    
def check_pemesanan_menu(transaction: Transaction):
    transaction.check_order()
    print("Total belanja yang harus dibayarkan adalah: Rp", transaction.item_total_price)

def switch(menu: int, transaction: Transaction):
    if menu == 1:
        add_item_menu(transaction)
    elif menu == 2:
        delete_item_menu(transaction)
    elif menu == 3:
        reset_menu(transaction)
    elif menu == 4:
        update_pemesanan_menu(transaction)
    elif menu == 5:
        check_pemesanan_menu(transaction)
    elif menu == 0:
        exit()
    else:
        print("Pilhan Tidak Ada")

def menu_selection(transaction):
    try:
        print('-'*50)
        print('{:<15}Pacmann Super Cashier'.format("", ""))
        print('-'*50)
        print("Pilih Menu:")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Reset Pemesanan")
        print("4. Update Item")
        print("5. Check Pemesanan")
        print("0. Keluar")
        print('-'*50)
        
        selected_menu = int(input("Pilihan Menu: "))
        
        switch(selected_menu, transaction)
        menu_selection(transaction)
    
    except:
        print("Input Invalid")

transaction = Transaction()
menu_selection(transaction)