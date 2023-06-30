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
            if inst.args[0] == 'duplicate_item':
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
            if inst.args[0] == 'not_found':
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
            if inst.args[0] == 'not_found':
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
            if inst.args[0] == 'not_found':
                print('Item yang akan diperbaharui tidak ditemukan')
