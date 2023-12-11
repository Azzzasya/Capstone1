#Capstone Modul 1-MEMBUAT APLIKASI DAFTAR NILAI DENGAN FITUR CRUD#
#Az Zahra Syahida-JCDS2204#
#Daftar Nilai Mahasiswa

from tabulate import tabulate
import getpass

### Code Yang berhubungan dengan Data ###
## Data Awal list dalam dictionary
data = {
    'NIM': [123130001, 123130002, 123130003],
    'Nama': ['Az Zahra Syahida', 'Linda Sulistyo', 'Nidaa Afifah'],
    'Tugas': [85.0, 75.0, 70.0],
    'UTS': [85.0, 40.0, 25.0],
    'UAS': [90.0, 80.0, 40.0],
    'Predikat': ['AB','BC','D'],
    'Keterangan': ['Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik',
                   'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik',
                   'Anda Tidak Lulus Mata Kuliah Pemrograman dan Metode Numerik']
}

## Fungsi Perhitungan 'nilai akhir, predikat, dan keterangan'
def hitung_predikat_keterangan(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    if nilai_akhir < 30:
        return 'E', 'Anda Tidak Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    elif 30.0 <= nilai_akhir < 50.0:
        return 'D', 'Anda Tidak Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    elif 50.0 <= nilai_akhir < 60.0:
        return 'C', 'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    elif 60.0 <= nilai_akhir < 70.0:
        return 'BC', 'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    elif 70.0 <= nilai_akhir < 80.0:
        return 'B', 'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    elif 80.0 <= nilai_akhir < 90.0:
        return 'AB', 'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik'
    else:
        return 'A', 'Anda Lulus Mata Kuliah Pemrograman dan Metode Numerik'

### Code yang berhubungan dengan Tampilan Menu ###

## Fungsi untuk menampilkan menu
def tampil_menu():
    print("\nDaftar Nilai Mata Kuliah Pemrograman dan Metode Numerik:")
    print("\nDosen : Dr. Achmad Kurniansyah")
    print("0. Keluar dari Akun")
    print("1. Keluar dari Program")
    print("2. Mengecek Nilai")
    print("3. Daftar Nilai Mahasiswa")
    print("4. Menambah Data Nilai Mahasiswa")
    print("5. Perbarui Nilai Mahasiswa")
    print("6. Hapus Data Mahasiswa")


## Fungsi memilih menu
def pilihan_menu():
    while True:

        pilihan_menu = int(input("Masukkan pilihan menu (0/00/1/2/3/4/5): "))
        if pilihan_menu in [0, 00, 1, 2, 3, 4, 5]:
            return pilihan_menu
        else:
            print("Silakan masukkan pilihan yang sesuai.")


## Fungsi tanya buat ke menu utama apa gak
def MenuutamaTANYA():
    # Tanyakan apakah pengguna ingin kembali ke menu utama atau keluar
    while True:
        choice = input("Pilihan: (y) Kembali ke menu utama, (n) Keluar dari program: ")
        if choice.lower() == "y":
            return 1 # Kembali ke menu utama
        elif choice.lower() == "n":
            return 2  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan pilih (y) atau (n).")


### Code untuk Login dan Logout ###
## Fungsi untuk login
def login():
    while True:
        # Meminta input dari pengguna
        username = int(input("Masukkan username: "))
        password = getpass.getpass(prompt="Password: ")
        try:
            # Conditional statement di login  
            if 123130001 <= username <= 123130150 and password == "mahasiswa" + str(username)[-4:]:
                return "Selamat datang, mahasiswa!"
            elif username == 111 and password == "dosen":
                return "Selamat datang, dosen!"
            else:
                print("Login gagal. Username atau password salah.")
        except:
            print("Terjadi kesalahan:")


# Variabel global untuk menyimpan informasi user yang sedang login
logged_in_user = None  # Inisialisasi dengan None

# Fungsi untuk logout
def logout():
    global logged_in_user  # Menandakan bahwa kita akan menggunakan variabel global
    logged_in_user = None
    print("Berhasil logout.")


### Segala Fungsi untuk di dalam Menu ###
## Fungsi untuk print Daftar Nilai Seluruh Mahasiswa
def printTabelNilai(data):
    # Menambahkan kolom "Predikat" dan "Keterangan"
    predikat_list = []
    keterangan_list = []
    for i in range(len(data['NIM'])):
        tugas = data['Tugas'][i]
        uts = data['UTS'][i]
        uas = data['UAS'][i]
        predikat, keterangan = hitung_predikat_keterangan(tugas, uts, uas)
        predikat_list.append(predikat)
        keterangan_list.append(keterangan)

    # Menambahkan list dari kamus
    data['Predikat'] = predikat_list
    data['Keterangan'] = keterangan_list
    
    # Data tupel di zip dan diubah ke bentuk list untuk dapat ditampilkan ke tabel
    tabelNilai = list(zip(data['NIM'], data['Nama'], data['Tugas'], data['UTS'], data['UAS'], data['Predikat'], data['Keterangan']))

    # Nama kolom di tabelnya 
    headers_tabelNilai = ['NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Predikat', 'Keterangan']

    # Mencetak tabel dengan tabulate
    print(tabulate(tabelNilai, headers=headers_tabelNilai, tablefmt='pretty'))

## Print sesuai input NIM
def printbarisNIM(data):
    username_input = int(input("Masukkan NIM: "))
    # Cari indeks NIM yang sesuai dalam daftar NIM
    try:
        nim_index = data['NIM'].index(username_input)
        headers_tabelNilai = ['NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Predikat', 'Keterangan']
        baris = [
            data['NIM'][nim_index], data['Nama'][nim_index],
            data['Tugas'][nim_index], data['UTS'][nim_index],
            data['UAS'][nim_index], data['Predikat'][nim_index],
            data['Keterangan'][nim_index]
        ]
        print(tabulate([baris], headers=headers_tabelNilai, tablefmt='pretty'))
    except ValueError:
        print("NIM mahasiswa tidak ditemukan.")

## Fungsi untuk mencetak 'tabel nilai' untuk mahasiswa yang lulus
def printTabelMahasiswaLulus(data):
    print("Daftar Mahasiswa yang Lulus Mata Kuliah Pemrograman dan Metode Numerik")
    # Menambahkan kolom "Predikat" dan "Keterangan"
    predikat_list = []
    keterangan_list = []
    for i in range(len(data['NIM'])):
        tugas = data['Tugas'][i]
        uts = data['UTS'][i]
        uas = data['UAS'][i]
        predikat, keterangan = hitung_predikat_keterangan(tugas, uts, uas)
        predikat_list.append(predikat)
        keterangan_list.append(keterangan)

    data['Predikat'] = predikat_list
    data['Keterangan'] = keterangan_list

    # Menambahkan list dari kamus
    tabelMahasiswaLulus = [baris for baris in zip(data['NIM'], data['Nama'], data['Tugas'], data['UTS'], data['UAS'], data['Predikat'], data['Keterangan'])
                           if baris[5] in ['C', 'BC', 'B', 'AB']]

    # Nama kolom tabel
    headers_tabelMahasiswaLulus = ['NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Predikat', 'Keterangan']

    # Mencetak tabel dengan tabulate
    print(tabulate(tabelMahasiswaLulus, headers=headers_tabelMahasiswaLulus, tablefmt='pretty'))


## Fungsi untuk mencetak 'tabel nilai' untuk mahasiswa yang tidak lulus
def printTabelMahasiswaTidakLulus(data):
    print("Daftar Mahasiswa yang Tidak Lulus Mata Kuliah Pemrograman dan Metode Numerik")
    # Menambahkan kolom "Predikat" dan "Keterangan"
    predikat_list = []
    keterangan_list = []
    for i in range(len(data['NIM'])):
        tugas = data['Tugas'][i]
        uts = data['UTS'][i]
        uas = data['UAS'][i]
        predikat, keterangan = hitung_predikat_keterangan(tugas, uts, uas)
        predikat_list.append(predikat)
        keterangan_list.append(keterangan)

    data['Predikat'] = predikat_list
    data['Keterangan'] = keterangan_list

    # Menambahkan list dari kamus
    tabelMahasiswaTidakLulus = [row for row in zip(data['NIM'], data['Nama'], data['Tugas'], data['UTS'], data['UAS'], data['Predikat'], data['Keterangan'])
                                if row[5] not in ['C', 'BC', 'B', 'AB']]

    # Nama kolom tabel
    headers_tabelMahasiswaTidakLulus = ['NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Predikat', 'Keterangan']

    # Mencetak tabel dengan tabulate
    print(tabulate(tabelMahasiswaTidakLulus, headers=headers_tabelMahasiswaTidakLulus, tablefmt='pretty'))


## Fungsi untuk Menambah data nilai mahasiswa
def MenambahNilai():
    print("Silahkan input Data Mahasiswa yang ingin ditambah:")
    nim = int(input("Masukkan NIM: "))

    # Memeriksa apakah NIM berada dalam rentang yang benar (123130001-123130150)
    if 123130001 <= nim <= 123130150:
        # Cek jika NIM sudah ada dalam data
        if nim in data['NIM']:
            print("Error: Mahasiswa dengan NIM tersebut sudah terdaftar.")
            return  # Menghentikan fungsi jika NIM sudah ada

        nama = input("Masukkan Nama: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))

        # Menambahkan data baru ke dalam dictionary
        data['NIM'].append(nim)
        data['Nama'].append(nama)
        data['Tugas'].append(tugas)
        data['UTS'].append(uts)
        data['UAS'].append(uas)

        # Menghitung predikat dan keterangan untuk data baru
        predikat, keterangan = hitung_predikat_keterangan(tugas, uts, uas)
        data['Predikat'].append(predikat)
        data['Keterangan'].append(keterangan)

        # Menampilkan tabel nilai terbaru
        printTabelNilai(data)
    else:
        print("Silahkan input NIM yang sesuai dalam rentang 123130001-123130150")

## Fungsi untuk memperbarui data mahasiswa
def updateDataMahasiswa(data):
    # Meminta input NIM dari dosen
    nim_mahasiswa = int(input("Masukkan NIM mahasiswa yang ingin di-update: "))

    # Cari indeks mahasiswa berdasarkan NIM
    index_mahasiswa = -1
    for i, nim in enumerate(data['NIM']):
        if nim == nim_mahasiswa:
            index_mahasiswa = i
            break

    # Periksa apakah NIM mahasiswa ditemukan
    if index_mahasiswa != -1:
        # Meminta input nilai baru
        tugas_baru = float(input("Masukkan nilai tugas baru: "))
        uts_baru = float(input("Masukkan nilai UTS baru: "))
        uas_baru = float(input("Masukkan nilai UAS baru: "))

        # Memperbarui nilai mahasiswa
        data['Tugas'][index_mahasiswa] = tugas_baru
        data['UTS'][index_mahasiswa] = uts_baru
        data['UAS'][index_mahasiswa] = uas_baru

        # Memanggil kembali fungsi hitung_predikat_keterangan untuk menghitung nilai predikat dan keterangan yang baru
        predikat_baru, keterangan_baru = hitung_predikat_keterangan(tugas_baru, uts_baru, uas_baru)
        
        # Memperbarui nilai predikat dan keterangan mahasiswa
        data['Predikat'][index_mahasiswa] = predikat_baru
        data['Keterangan'][index_mahasiswa] = keterangan_baru

        # Menampilkan hasil pembaruan
        print("Data mahasiswa berhasil di-update:")
        printTabelNilai(data)
        print(f"Predikat dan keterangan baru untuk mahasiswa dengan NIM {nim_mahasiswa}: {predikat_baru}, {keterangan_baru}")
    else:
        print("NIM mahasiswa tidak ditemukan.")


## Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapusDataMahasiswa(data):
    # Minta input NIM mahasiswa yang akan dihapus
    nim_mahasiswa_hapus = int(input("Masukkan NIM mahasiswa yang akan dihapus: "))

    # Cari indeks mahasiswa berdasarkan NIM
    index_mahasiswa = -1
    for i, nim in enumerate(data['NIM']):
        if nim == nim_mahasiswa_hapus:
            index_mahasiswa = i
            break

    # Periksa apakah NIM mahasiswa ditemukan
    if index_mahasiswa != -1:
        # Hapus data mahasiswa
        data['NIM'].pop(index_mahasiswa)
        data['Nama'].pop(index_mahasiswa)
        data['Tugas'].pop(index_mahasiswa)
        data['UTS'].pop(index_mahasiswa)
        data['UAS'].pop(index_mahasiswa)
        data['Predikat'].pop(index_mahasiswa)
        data['Keterangan'].pop(index_mahasiswa)

        print(f"Data mahasiswa dengan NIM {nim_mahasiswa_hapus} berhasil dihapus.")
    else:
        print("NIM mahasiswa tidak ditemukan.")

Menu = True
while Menu:
    hasil_login = login()
    if hasil_login.startswith("Selamat datang"):
        cond = True
        while cond:
            try:
                tampil_menu()
                choice = pilihan_menu()
                
                if hasil_login.startswith("Selamat datang, mahasiswa"):
                    if choice not in [0,00,1, 2]:
                        print("Akses ditolak. Mahasiswa hanya dapat mengakses menu 1 dan 2.")
                        continue  # Kembali ke tampilan menu
                if choice == 0:
                    # Fungsi Logout di sini
                    logout() # Menampilkan hasil logout
                    back = MenuutamaTANYA()
                    if back == 1 :
                        print("Silahkan Login sebelum masuk ke menu utama")
                        break
                    elif back == 2 :
                        Menu = False
                        break
                elif choice == 1: # Keluar dari Program
                    Menu = False
                    break
                elif choice == 2:
                    printbarisNIM(data)
                    back = MenuutamaTANYA()
                    if back == 2:
                        Menu = False
                        break
                elif choice == 3:
                    print('''a. Daftar Nilai Mahasiswa Keseluruhan \n b. Daftar Nilai Mahasiswa yang Lulus \n c. Daftar Nilai Mahasiswa yang Tidak Lulus''')
                    sub_choice = input("Pilih submenu (a, b, c): ")
                    if sub_choice.lower() == "a":
                        printTabelNilai(data) 
                        back = MenuutamaTANYA()
                        if back == 2:
                            Menu = False
                            break
                    elif sub_choice.lower() == "b":
                        printTabelMahasiswaLulus(data) 
                        back = MenuutamaTANYA()
                        if back == 2:
                            Menu = False
                            break
                    elif sub_choice.lower() == "c":
                        printTabelMahasiswaTidakLulus(data)
                        back = MenuutamaTANYA()
                        if back == 2:
                            Menu = False
                            break
                    else:
                        print("Pilihan submenu tidak valid.")
                elif choice == 4:
                    MenambahNilai()
                    back = MenuutamaTANYA()
                    if back == 2:
                        Menu = False
                        break
                elif choice == 5:
                    printTabelNilai(data)
                    updateDataMahasiswa(data)
                    back = MenuutamaTANYA()
                    if back == 2:
                        Menu = False
                        break
                elif choice == 6:
                    printTabelNilai(data)
                    hapusDataMahasiswa(data)
                    back = MenuutamaTANYA()
                    if back == 2:
                        Menu = False
                        break
            except:
                print("Pilihan menu tidak valid. Silakan pilih menu yang sesuai.")
    else:
        print("Login gagal. Program berhenti.")