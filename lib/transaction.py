class Transaction:
    def __init__(self):
        self.item_list = []
    
    def add_item(self, item_name=None, quantity=None, price=None):
        try:
            if(item_name==None or quantity==None or price==None):
                raise Exception("missing_field")
            
            for item in self.item_list:
                if item['name'] == item_name:
                    raise Exception('duplicate_item')
            
            self.item_list.append({'name':item_name, 'quantity':quantity, 'price':price})
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item, kuantitas, dan harga.')
            elif inst.args[0] == 'duplicate_item':
                print('Sudah ada item dengan nama yang sama.')

    def update_item_name(self, item_name=None, updated_name=None):
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
    
    def update_item_quantity(self, item_name=None, updated_quantity=None):
        try:
            found_flag = False
            
            if(item_name==None or updated_quantity==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    item['quantity'] = updated_quantity
                    found_flag = True
                    break
                
            if(not found_flag):
                raise Exception('not_found')
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item dan kuantitas yang akan diperbaharui.')
            elif inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')

    def update_item_price(self, item_name=None, price=None):
        try:
            found_flag = False
            
            if(item_name==None or price==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    item['price'] = price
                    found_flag = True
                    break
                
            if(not found_flag):
                raise Exception('not_found')
            
        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item dan harga yang akan diperbaharui.')
            elif inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')

    def delete_item(self, item_name=None):
        try:
            found_flag = False
            
            if(item_name==None):
                raise Exception('missing_field')
            
            for item in self.item_list:
                if item['name'] == item_name:
                    self.item_list.remove(item)
                    found_flag = True
                    break
                
            if(not found_flag):
                raise Exception('not_found')

        except Exception as inst:
            if inst.args[0] == 'missing_field':
                print('Pastikan memasukkan nama item yang akan dihapus.')
                
            elif inst.args[0] == 'not_found':
                print('Item yang akan dihapus tidak ditemukan.')
                
    def reset_transaction(self):
        try:
            self.item_list = []

        except:
            print('Terdapat kesalahan saat me-reset transaksi.')
                
                
    def check_order(self):
        try:
            missing_property_flag = False
            
            headers = ['Nama Item', 'Jumlah Item', 'Harga/Item', 'Total Harga']
            print("{:<20} | {:<15} | {:<15} | {:<10}".format(headers[0], headers[1], headers[2], headers[3]))
            print("-" * 70)

            for item in self.item_list:
                if('name' not in item or 'quantity' not in item or 'price' not in item):
                    missing_property_flag = True
                else:
                    print("{:<20} | {:<15} | {:<15} | {:<10}".format(item['name'], item['quantity'], item['price'], item['quantity'] * item['price']))
                    
            if(missing_property_flag):
                raise Exception("missing_property")
            else:
                print("Pemesanan sudah benar.")

        except Exception as inst:
            if inst.args[0] == 'missing_property':
                print('Pemesanan salah. Terdapat Item yang belum memiliki informasi lengkap.')
