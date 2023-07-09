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
#### Main Menu
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/71c75d23-a650-4cef-9240-54f52d585df5" width="600px"/>  
  
Main menu merupakan tampilan utama dari sistem yang dibuat dimana pengguna akan berinteraksi dengan sistem dan memberi masukan untuk menjalankan tiap fungsi yang ada. Main menu akan menerima masukan berupa pilihan menu dari pengguna. Kemudian berdasarkan pilihan menu pengguna tersebut akan mengeksekusi fungsi-fungsi yang telah ditentukan sebelumnya. Proses ini diulangi hingga pengguna menyelesaikan transaksi.

#### Add Item
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/2338411b-4061-413a-9e00-7f125ea91352" width="400px"/>  
  
Gambar diatas merupakan flowchart untuk fungsi "Add Item" yang digunakan untuk menambahkan item pada transaksi saat ini. Pada fungsi "Add Item", masukan yang diterima adalah nama item, harga, dan jumlah yang merepresentasikan sebuah item. Setelah itu, dilakukan pengecekan apakah ketiga masukan tersebut telah dimasukan semuanya. Jika belum, maka akan menampilkan pesan error dan pengguna diminta untuk mengulangi masukan, sedangkan jika sudah semua, maka item tersebut akan ditambahkan ke daftar item

#### Update Item Name
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/914b6caf-b7ad-4d22-b86e-27742a118605" width="400px"/>

Gambar diatas merupakan flowchart untuk fungsi "Update Item Name" yang digunakan untuk memperbaharui sebuah nama item. Masukan yang diterima adalan nama item yang akan diupdate dan update nama yang akan dilakukan. Dari kedua masukan akan dicek, jika terdapat masukan yang belum diberikan, maka akan menampilkan pesan error. Jika keseluruhan masukan sudah diberikan, maka dilanjutkan dengan pengecekan apakah nama item terdapat pada daftar item. Jika iya maka dilakukan update nama, sedangkan jika tidak maka akan menampilkan pesan error.

#### Update Item Quantity
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/b86b2349-a468-4cbe-bca2-f71d03f36fe7" width="400px"/>
  
Gambar diatas merupakan flowchart untuk fungsi "Update Item Quantity" yang digunakan untuk memperbaharui kuantitas sebuah item. Masukan yang diterima adalan nama item yang akan diupdate dan update kuantitas yang akan dilakukan. Dari kedua masukan akan dicek, jika terdapat masukan yang belum diberikan, maka akan menampilkan pesan error. Jika keseluruhan masukan sudah diberikan, maka dilanjutkan dengan pengecekan apakah nama item terdapat pada daftar item. Jika iya maka dilakukan update kuantitas, sedangkan jika tidak maka akan menampilkan pesan error.

#### Update Item Price
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/2c7d2df9-6a49-45cb-8053-f6a00755f6b7" width="400px"/>
  
Gambar diatas merupakan flowchart untuk fungsi "Update Item Price" yang digunakan untuk memperbaharui harga sebuah item. Masukan yang diterima adalan nama item yang akan diupdate dan update harga yang akan dilakukan. Dari kedua masukan akan dicek, jika terdapat masukan yang belum diberikan, maka akan menampilkan pesan error. Jika keseluruhan masukan sudah diberikan, maka dilanjutkan dengan pengecekan apakah nama item terdapat pada daftar item. Jika iya maka dilakukan update harga, sedangkan jika tidak maka akan menampilkan pesan error.

#### Delete Item
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/e643645c-b5f1-4f1d-8473-4861c338fade" width="400px"/>
  
Gambar diatas merupakan flowchart untuk "Delete Item" yang digunakan untuk menghapus sebuah item. Pada "Delete Item" masukan yang diterima adalah sebuah nama dari item yang akan dihapus. Jika nama item tidak diberikan maka akan menampilkan pesan error dan pengguna diminta untuk memasukan kembali, sedangkan jika diberikan maka akan dilakukan pengecekan berikutnya. Pengecekan berikutnya yang dilakukan adalah mengecek apakah nama item yang akan dihapus terdapat pada daftar item. Jika ada, maka item tersebut akan dihapus dari daftar item, sedangkan jika tidak maka akan menampilkan pesan error tidak ditemukan.

#### Reset
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/f5ac26d2-332e-43cb-8a03-19261d863c58" width="200px"/>
  
Gambar diatas merupakan flowchart untuk "Reset". Setelah "Reset" dieksekusi maka kondisi transaksi dikembalikan seperti semula, saat transaksi baru dinisiasi.

#### Check Order
<img src="https://github.com/agastiayudya/Pacmann-Cashier/assets/96803882/682c63af-5d09-47bc-8569-cee2ce9b881b" width="400px"/>

Gambar diatas merupakan flowchart untuk "Check Order" yang digunakan untuk menampilkan item yang telah dimasukkan pada transaksi saat ini dan melakukan pengecekan apakah terdapat item dengan informasi diperlukan yang masih kosong. "Check Order" akan melakukan perulangan untuk mengecek seluruh item yang ada di transaksi saat ini. Pada "Check Order" terdapat flag khusus yang disebut dengan "Missing Flag". Missing Flag ini digunakan untuk memberi tanda apakah terdapat item yang masih belum lengkap informasinya atau tidak. Jika True berarti masih terdapat item yang belum lengkap.
  
Pada tiap perulangan item, dicek apakah item tersebut memiliki seluruh informasi yang diperlukan. Jika tidak, maka "Missing Flag" dibuat True. Setelah dicek, maka item akan ditampilkan. Setelah pengecekan keseluruhan item selesai, maka akan ditampilkan informasi tambahan berdasarkan "Missing Flag". Jika "Missing Flag" bernilai False maka ditampilkan order benar, sedangkan jika tidak maka ditampilkan order salah.

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
