PANDUAN MENJALANKAN VENDING MACHINE DFA

Program ini dibuat dengan bahasa Pemrograman Python. Untuk menjalankan program berjalan dengan baik, maka dapat diperhasikan petunjuk di bawah ini : 

----Persiapan File 
1. vending_dfa.txt 
merupakan file yang berisi transisi DFA beserta start state, dan input yang diterima

2. vendingmachine.py 
merupakan file yang berisi program vending machine tanpa poin bonus (ketika uang yang dimasukkan berlebih dari harga minuman, maka transaksi tidak bisa diproses)

3. VendingMchine_bonus.py
merupakan file yang berisi program vending machine dengan poin bonus (ketika uang yang dimasukkan berlebih dari harga minuman, maka transaksi dapat diproses dan menghasilkan kembalian)

MENJALANKAN FILE PYTHON
---Cara Menjalankan Program vendingmachine.py
1. Buka Terminal pada direktori yang sama dengan vendingmachine.py

2. Jalankan Program
perintah untuk menjalankan program: python vendingmachine.py

---Cara Menjalankan Program VendingMachine_bonus.ph
1. Buka Terminal pada direktori yang sama dengan VendingMachine_bonus.py

2. Jalankan Program
perintah untuk menjalankan program: python VendingMachine_bonus.py

MENJALANKAN FILE EXECUTABLE (.exe)
Untuk Windows : 
-Download file vendingmachine.exe dan VendingMachine_bonus.exe
-Pastikan file vending_dfa.txt berada di folder yang sama
-Klik double pada vendingmachine.exe atau VendingMachine_bonus.exe

Untuk Linux/Mac:
-Download file executable yang sesuai
-Berikan permission eksekusi
    chmod +x vendingmachine atau
    chmod +x VendingMachine_bonus atau
-Jalankan
    ./vendingmachine atau
    ./VendingMachine_bonus

Catatan Penting : 
-Pastikan sudah menginstall Python untuk menjalankan file python
-Pastikan file vending_dfa.txt berada dalam folder yang sama dengan file executable vendigmachine.exe dan VendingMachine_bonus.exe 
- Input uang yang diterima : 
1000, 2000, 5000, 10000
- Input minuman yang diterima : 
A, B, C (pastikan huruf kapital)

Untuk input selain yang tercantum di atas akan dianggap tidak valid. 
