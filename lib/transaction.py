class Transaction:
    """
        Class untuk merepresentasikan setiap transaksi yang dilakukan di kasir.
        
        Property:
            - item_list = Daftar item yang dimasukkan di transaksi terkait
            - item_total_price = Total harga keseluruhan item
        
        Method:
            - add_item = Menambahkan item ke 'item_list'
            - update_item_name = Memperbaharui nama item yang terdapat pada 'item_list'
            - update_item_quantity = Memperbaharui kuantitas item yang terdapat pada 'item_list'
            - update_item_price = Memperbaharui harga item yang terdapat pada 'item_list'
            - delete_item = Menghapus item yang terdapat pada 'item_list'
            - reset_transaction = Menghapus seluruh item pada 'item_list'
            - check_order = Mengecek dan menampilkan item pada 'item_list'
            - total_price = Menghitung total harga dan menyimpan pada 'item_total_price'
    """
    
    def __init__(self):
        self.item_list = []
        self.item_total_price = 0
    
    def add_item(self, item_name:str=None, quantity:int=None, price:float=None):
        """
            Menambahkan item pada 'item_list'
            
            Parameters:
                - item_name: string = Nama item yang akan ditambahkan
                - quantity: integer = Kuantitas item yang akan ditambahkan
                - price: float = Harga item yang akan ditambahkan
            
            Return: None
        """
        try:
            if(item_name==None or quantity==None or price==None):
                raise Exception("missing_field")
            
            for item in self.item_list:
                if item['name'] == item_name:
                    raise Exception('duplicate_item')
            
            self.item_list.append({'name':item_name, 'quantity':quantity, 'price':price})
            self.total_price()
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item, kuantitas, dan harga.')
            elif inst.args[0] == 'duplicate_item':
                print('Sudah ada item dengan nama yang sama.')

    def update_item_name(self, item_name:str=None, updated_name:str=None):
        """
            Memperbaharui nama item yang terdapat pada 'item_list'. Pencocokan item didasarkan pada nama item.
            
            Parameters:
                - item_name: string = Nama item yang akan diperbaharui
                - updated_name: string = Nama baru dari item yang dipilih
            
            Return: None
        """
        try:
            found_flag = False
            
            if(item_name==None or updated_name==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    item['name'] = updated_name
                    found_flag = True
                    break
                
            if(not found_flag):
                raise Exception('not_found')
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item dan nama yang akan diperbaharui.')
            elif inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')
    
    def update_item_quantity(self, item_name:str=None, updated_quantity:int=None):
        """
            Memperbaharui kuantitas item yang terdapat pada 'item_list'. Pencocokan item didasarkan pada nama item.
            
            Parameters:
                - item_name: string = Nama item yang akan diperbaharui
                - updated_quantity: integer = Kuantitas baru dari item yang dipilih
            
            Return: None
        """
        
        try:
            found_flag = False
            
            if(item_name==None or updated_quantity==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    item['quantity'] = updated_quantity
                    found_flag = True
                    self.total_price()
                    break
                
            if(not found_flag):
                raise Exception('not_found')
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item dan kuantitas yang akan diperbaharui.')
            elif inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')

    def update_item_price(self, item_name:int=None, price:float=None):
        """
            Memperbaharui harga item yang terdapat pada 'item_list'. Pencocokan item didasarkan pada nama item.
            
            Parameters:
                - item_name: string = Nama item yang akan diperbaharui
                - price: integer = Harga baru dari item yang dipilih
            
            Return: None
        """
        
        try:
            found_flag = False
            
            if(item_name==None or price==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    item['price'] = price
                    found_flag = True
                    self.total_price()
                    break
                
            if(not found_flag):
                raise Exception('not_found')
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item dan harga yang akan diperbaharui.')
            elif inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')

    def delete_item(self, item_name:str=None):
        """
            Menghapus item yang terdapat pada 'item_list' berdasarkan nama item.
            
            Parameters:
                - item_name: string = Nama item yang akan dihapus
            
            Return: None
        """
        try:
            found_flag = False
            
            if(item_name==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    self.item_list.remove(item)
                    found_flag = True
                    self.total_price()
                    break
                
            if(not found_flag):
                raise Exception('not_found')

        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item yang akan dihapus.')
                
            elif inst.args[0] == 'not_found':
                print('Item yang akan dihapus tidak ditemukan.')
                
    def reset_transaction(self):
        """
            Menghapus seluruh item pada 'item_list', mengembalikan 'item_total_price' menjadi 0.
            
            Parameters: None
            
            Return: None
        """
        
        try:
            self.item_list = []
            self.total_price()

        except:
            print('Terdapat kesalahan saat me-reset transaksi.')
                
                
    def check_order(self):
        """
            Mengecek dan menampilkan seluruh item pada 'item_list'. Item dicek berdasarkan ketersediaan property 'name', 'quantity', dan 'price' pada tiap item.
            
            Parameters: None
            
            Return: None
        """
        
        try:
            missing_property_flag = False
            
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print("{:<20} | {:<15} | {:<15} | {:<10}".format(headers[0], headers[1], headers[2], headers[3]))
            print("-" * 70)

            for item in self.item_list:
                if('name' not in item or 'quantity' not in item or 'price' not in item):
                    missing_property_flag = True
                    
                print("{:<20} | {:<15} | {:<15} | {:<10}".format(item['name'], item['quantity'], item['price'], item['quantity'] * item['price']))
                    
            if(missing_property_flag):
                raise Exception("missing_property")
            else:
                print("Pemesanan sudah benar.")

        except Exception as inst:
            if inst.args[0] == 'missing_property':
                print('Pemesanan salah. Terdapat Item yang belum memiliki informasi lengkap.')

    def total_price(self):
        """
            Menghitung total harga dari seluruh item pada item_list dan menghitung diskon berdasarkan aturan yang telah ditetapkan.
            Hasil perhitungan akan disimpan pada 'item_total_price'.
            
            Parameters: None
            
            Return: None
        """
        self.item_total_price = 0
        
        if(len(self.item_list) > 0):
            for item in self.item_list:
                self.item_total_price += item['quantity'] * item['price']
        
        if self.item_total_price > 500000:
           self.item_total_price *= (1.0 - 0.10)
        elif self.item_total_price > 300000:
           self.item_total_price *= (1.0 - 0.08)
        elif self.item_total_price > 200000:
           self.item_total_price *= (1.0 - 0.05)
