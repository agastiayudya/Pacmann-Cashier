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

