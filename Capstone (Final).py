#
sumber_data = [
    {'NoPol'        :'B 6843 SS',
     'Jenis Mobil'  :'Pajero', 
     'Transmisi'    :'Matic', 
     'Harga'        :700000,
     'Status'       :'Available'},

    {'NoPol'        :'D 7901 PQ', 
    'Jenis Mobil'   :'Ertiga', 
    'Transmisi'     :'Matic', 
    'Harga'         :450000,
    'Status'        :'Available'},
    
    {'NoPol'        :'B 5721 LP', 
    'Jenis Mobil'   :'Avanza', 
    'Transmisi'     :'Manual', 
    'Harga'         :150000,
    'Status'        :'Available'},
    
    {'NoPol'        :'B 8780 HH', 
    'Jenis Mobil'   :'Brio', 
    'Transmisi'     :'Manual', 
    'Harga'         :300000,
    'Status'        :'Available'}
]

#Fungsi Untuk Menu Utama
def daftar_menu():
    print(f'''
    ==================================
    **********************************
    ----------------------------------        
    SELAMAT DATANG DI PT. AUTO MOTORS
    ----------------------------------
    **********************************
    ==================================
    Menu Utama:

    1. Laporan Data Mobil
    2. Menambahkan Data Mobil
    3. Memperbarui Data Mobil
    4. Menghapus Data Mobil
    0. Exit 
    ''')
#Fungsi Untuk Menu 1
def menu1():
    while True:
        print(f'''
        ^^^^^^^^^^^^^^^^^^^^^^^
             DAFTAR MENU 1
        ^^^^^^^^^^^^^^^^^^^^^^^
        1. Daftar Seluruh Mobil
        2. Daftar Transmisi
        3. Kembali ke Menu Utama 
        ''')
        pilih_menu1 = int(input('Masukkan Pilihan Anda: \n'))
        if pilih_menu1 == 1:
            daftar_mobil()     
        elif pilih_menu1 == 2:
            daftar_transmisi()
            break
            
            
        elif pilih_menu1 == 3:
            break
        else:
            print('^^^^Menu yang dimasukkan tidak tersedia^^^^')
            continue

#Fungsi Untuk Menu 2
def menu2():
    while True:
        print(f'''
        ^^^^^^^^^^^^^^^^^^^^^^^
             DAFTAR MENU 2
        ^^^^^^^^^^^^^^^^^^^^^^^
        1. Tambah Data Mobil
        2. Kembali ke Menu Utama
        ''')
        pilih_menu2 = int(input('Masukkan Pilihan Anda: \n'))
        if pilih_menu2 ==1:
            tambah_mobil()
        elif pilih_menu2 == 2:
            break
        else:
            print('^^^^Menu yang dimasukkan tidak tersedia^^^^')
            continue

#Fungsi Untuk Menu 3
def menu3():
    while True:
        print(f'''
        ^^^^^^^^^^^^^^^^^^^^^^^
             DAFTAR MENU 3
        ^^^^^^^^^^^^^^^^^^^^^^^
        1. Perbarui Data Mobil
        2. Kembali ke Menu Utama 
        ''')
        pilih_menu3 = int(input('Masukkan Pilihan Anda: \n'))
        if pilih_menu3 == 1:
            ubah_mobil()
        elif pilih_menu3 == 2:
            break
        else:
            print('^^^^Menu yang dimasukkan tidak tersedia^^^^')
            continue

#Daftar Untuk Menu 4
def menu4():
    while True:
        print(f'''
        ^^^^^^^^^^^^^^^^^^^^^^^
             DAFTAR MENU 4
        ^^^^^^^^^^^^^^^^^^^^^^^
        1. Hapus Data Mobil
        2. Kembali ke Menu Utama 
        ''')
        pilih_menu4 = int(input('Masukkan Pilihan Anda: \n'))
        if pilih_menu4 ==1:
            hapus_mobil()
        elif pilih_menu4 ==2:             
            break
        else:
            print('^^^^Menu yang dimasukkan tidak tersedia^^^^')
            continue

#Daftar untuk bagian yang ingin di ubah Menu 3
def perbarui_daftar():
    print(f'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Data Mana yang Ingin Diperbarui?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. No. Polisi
2. Jenis Mobil
3. Transmisi
4. Harga 
5. Status Mobil 
0. Kembali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')
        
#Untuk data yang berhasil di ubah
def berhasil():
    daftar_mobil()
    print('\n^^^^^^^^^^^^^^^^^^^^^^^^\nData Berhasil Diperbarui\n^^^^^^^^^^^^^^^^^^^^^^^^')

#Untuk hasil print data tidak jadi di ubah
def gagal():
    print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^\nData Tidak Berhasil Diperbarui\n^^^^^^^^^^^^^^^^^^^^^^^^^^')
    
#Memunculkan Data Mobil Keseluruhan 
def daftar_mobil():
    print('\n                 DAFTAR MOBIL PT. AUTO MOTORS\n-------------------------------------------------------------')
    print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
    No = 1
    for i in sumber_data:
        print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")
        No = No+1

#Memunculkan Data Mobil Matic atau Manual 
def daftar_transmisi():
    transmisi_user = input('Masukkan Transmisi Mobil: \n').capitalize()
    if transmisi_user not in [i['Transmisi'] for i in sumber_data]:
        print ('\n^^^^Mobil Tidak Tersedia^^^^')
    else:
        No = 1
        print('\n                       PT. AUTO MOTORS \n-------------------------------------------------------------')
        print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
        for i in sumber_data :
            if (i['Transmisi']) == transmisi_user:
                # Print Header 
                print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")
                No = No+1

#Menambahkan Data Mobil yang Belum Ada 
def tambah_mobil():
    add_NoPol_user = input('Masukkan Plat Mobil: \n').upper()
    for i in sumber_data: #Jika data nopol sama dengan yang sudah dibuat di (sumber_data)
        if (i['NoPol']) == add_NoPol_user:
            print(f''' 
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    Mobil Sudah Ada
            Silahkan Periksa pada Sumber Data!
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        else:
            nopol = input('Masukkan no. polisi mobil yang ingin ditambahkan: \n').upper()
            jenis = input('Masukkan jenis mobil: \n').capitalize()
            transmisi = input('Masukkan jenis transmisi mobil: \n').capitalize()
            harga = int(input('Masukkan harga sewa harian: \n'))
            status = input('Masukkan status mobil: \n').capitalize()
            cek = input('Apakah Anda yakin ingin menambahkan data ini? (Y/N)').upper()
            if cek == 'Y':
                tambahan_daftar_mobil = {'NoPol':nopol,'Jenis Mobil':jenis,'Transmisi':transmisi, 'Harga':harga, 'Status':status}
                sumber_data.append(tambahan_daftar_mobil)
                daftar_mobil()
                break
            else:
                print(f'''
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Data Tidak Berhasil Diperbarui
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ''')
                break

#Mengubah Data Mobil yang Sudah Ada (UPDATE)
def ubah_mobil():
    daftar_mobil()
    while True:
        ubah_no_baris = int(input('\n Masukkan no. baris yang ingin di ubah: \n'))
        if ubah_no_baris not in range(1, len(sumber_data)+1):
            print('Tidak ada data pada baris tersebut')
            continue
        else:
            cek2 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
            if cek2== 'Y':
                perbarui_daftar()
                ubah_data = int(input('Pilih data yang ingin diubah: \n'))
                if ubah_data == 1:
                    ubah_nopol = input('Masukkan No.Polisi Baru: \n').upper()
                    cek3 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        sumber_data[ubah_no_baris-1]['NoPol'] = ubah_nopol
                        berhasil()
                        break
                    else:
                        gagal()
                        continue 
                elif ubah_data == 2:
                    jenis_ubah = input('Masukkan Jenis Mobil Baru: \n').capitalize()
                    cek3 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        sumber_data[ubah_no_baris-1]['Jenis Mobil'] = jenis_ubah
                        berhasil()
                        break
                    else:
                        gagal()
                        continue 
                elif ubah_data == 3:
                    ubah_transmisi = input('Masukkan Transmisi Mobil Baru: \n').capitalize()
                    cek3 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        sumber_data[ubah_no_baris-1]['Transmisi'] = ubah_transmisi
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif ubah_data == 4:
                    ubah_harga = int(input('Masukkan Harga Sewa Mobil Baru: \n'))
                    cek3 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        sumber_data[ubah_no_baris-1]['Harga'] = ubah_harga
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif ubah_data == 5:
                    ubah_status = input('Masukkan Status Mobil Saat Ini: ').title()
                    cek3 = input('Apakah Anda yakin ingin ubah data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        sumber_data[ubah_no_baris-1]['Status'] = ubah_status
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif ubah_data == 0:
                    break
                else:
                    print('Menu yang dimasukkan tidak tersedia')
                    continue
            else :
                print('Data tidak jadi diubah')
                break 

#Menghapus Data Mobil 
def hapus_mobil():
    daftar_mobil()
    while True:
        hapus_baris = int(input('\n Masukkan no. baris yang ingin dihapus: '))
        if hapus_baris not in range(1, len(sumber_data)+1):
            print()
            print('^^^^Tidak sesuai dengan no. baris pada Daftar Mobil PT. Auto Motors^^^^')
            continue
        else:
            cek = str(input('\n Apakah Anda yakin ingin menghapus data? (Y/N) ')).capitalize()
            if (cek == 'Y'):
                del sumber_data[hapus_baris-1]
                daftar_mobil()
                print('\n^^^^Data berhasil dihapus^^^^\n')
                break
            else:
                print()
                print('^^^^Data tidak berhasil dihapus^^^^')
                break

#Menu Utama
while True:
    daftar_menu()
    menu_utama = int(input ('Masukkan Pilihan Anda: \n'))
    if menu_utama == 1:
        menu1()    
    elif menu_utama == 2:
        menu2()
    elif menu_utama == 3:
        menu3()
    elif menu_utama == 4:
        menu4()
    elif menu_utama == 0:
        keluar = input('\n Apakah Anda yakin ingin keluar? (Y/N) ').capitalize()
        if keluar == 'Y':
            print()
            print('^^^^Harga Rental Mobil Terhitung Per Hari Ya!^^^^')
            print()
            print('^^^^Terima Kasih & Hati-hati Dijalan!!^^^^')
            break
        else:
            continue
    else:
        print()
        print('^^^^Menu yang dimasukkan tidak tersedia^^^^')
        print()
        continue                                                                                                                                                                     