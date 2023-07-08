### Project Background
Seorang pemilik supermarket besar di suatu kota di Indonesia memerlukan perbaikan dalam proses bisnisnya dengan membuat sistem kasir 
yang self-service di supermarket miliknya. Dalam sistem sel-service tersebut customer bisa langsung memasukkan item yang dibeli, 
jumlah item yang dibeli, dan harga item yang dibeli, serta fitur lain. Hal ini akan memudahkan customer yang tidak berada di kota 
yang sama juga dapat membeli barang di supermarket tersebut. Oleh karena itu, perlu dibuat program yang memuat fitur-fitur agar 
sistem kasir self-service tersebut terealisasikan.

### Objectives
Tujuan dari program self-service cashier ini adalah:
1. Mengautomasi sistem kasir sehingga meningkatkan efisiensi proses transaksi
2. Memperbaiki pengalaman pelanggan karena memberikan kenyaman dan kecepatan dalam berbelanja
3. Meningkatkan aksesibilitas bagi pelanggan jarak jauh karena tidak perlu datang langsung untuk berbelanja

### Flowchart
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/71c75d23-a650-4cef-9240-54f52d585df5)
xxxxxx
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/2338411b-4061-413a-9e00-7f125ea91352)
xxxxx

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/914b6caf-b7ad-4d22-b86e-27742a118605)

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/b86b2349-a468-4cbe-bca2-f71d03f36fe7)

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/2c7d2df9-6a49-45cb-8053-f6a00755f6b7)

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/e643645c-b5f1-4f1d-8473-4861c338fade)

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/f5ac26d2-332e-43cb-8a03-19261d863c58)

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/682c63af-5d09-47bc-8569-cee2ce9b881b)

### Penjelasan Functions 
Terdapat class transaction.py yang bertujuan untuk merepresentasikan setiap transaksi yang dilakukan di kasir.
Dalam class tersebut terdapat property item_list dan item_total_price dengan penjelasan masing-masing sebagai berikut:
- item_list = Daftar item yang dimasukkan di transaksi terkait
- item_total_price = Total harga keseluruhan item
        
Di dalam class transaction.py terdapat beberapa fungsi dengan penjelasan sebagai berikut:
- add_item = Menambahkan item ke 'item_list'
- update_item_name = Memperbaharui nama item yang terdapat pada 'item_list'
- update_item_quantity = Memperbaharui kuantitas item yang terdapat pada 'item_list'
- update_item_price = Memperbaharui harga item yang terdapat pada 'item_list'
- delete_item = Menghapus item yang terdapat pada 'item_list'
- reset_transaction = Menghapus seluruh item pada 'item_list'
- check_order = Mengecek dan menampilkan item pada 'item_list'
- total_price = Menghitung total harga dan menyimpan pada 'item_total_price'

### Demonstrasi output code test case
1. Test case 1
- Isi code:

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/928dd418-cb78-429e-9cfa-77d1b661ed5d)
- Output test case 1:
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/f8cdc869-dccd-4c96-a557-194c17e9360a)

2. Test case 2
- Isi code:

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/5393d517-0888-4c2e-8365-65df7e2dcab0)
- Output test case 2:
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/73f20fc2-2060-4f4d-a5df-ef465dc90739)
 
3. Test case 3
- Isi code:

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/705016bd-328f-4c3f-842b-ecefbe0f92f0)
- Output test case 3:
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/57736314-86d2-4368-b0a5-8dbd22785b0e)

4. Test case 4
- Isi code:

![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/e8f7bba5-26de-4456-b08d-0e850c5ccdd5)

- Output test case 4:
![image](https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/39650852-338d-4f85-9c7b-4316d9046efb)

### Conclusion
Program super cashier berhasil dijalankan dan telah lolos dari test case yang diberikan.
