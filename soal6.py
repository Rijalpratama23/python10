# membuat prrogram pemminjaman buku
dataBuku = []
dataMahasiswa = []
dataPinjam = []

def tambahBuku ():
    buku = {
        "no_isbn":input("masukan No.Isbn buku : "),
        "judul": input("masukan judul Buku : "),
        "pengarang":input("masukan pengarang : "),
        "isiHalaman":int(input("masukan isi halaman : ")),
        "deskripsi":input("masukan deskripsi : "),
        "stok": int(input("masukan jumlah stok : ")),
        "dipinjam": 0
    }
    dataBuku.append(buku)
    print("Selamat, Buku berhasil di tambahkan!")

def tambahMahasiswa ():
    mahasiswa = {
        "nama":input("masukan nama anda :"),
        "nim": input("masukan NIM : "),
        "noHP": input("masukan Nomor HP Anda : "),
        "alamat":input("masukan alamat : ")
    }
    dataMahasiswa.append(mahasiswa)
    print("data mahasiswa berhasil di tambahkan !!")

def pinjamBuku ():
    nim = input("Masukan NIM Anda : ")
    no_isbn = input("Masukan nomor ISBN buku : ")
    tanggalPinjam = int(input("Masukan Tanggal Pinjam (YYYY-MM-DD) : "))
    tanggalKembali = int(input("Masukan Tanggal Kembali (YYYY-MM-DD) : "))
    status = "dipinjam"
    pinjam = {
        "nim": nim,
        "no_isbn": no_isbn,
        "tanggalPinjam": tanggalPinjam,
        "tanggalKembali": tanggalKembali,
        "status": status
    }
    dataPinjam.append(pinjam)
    print("Buku telah berhasil di pinjam !!!")

while True:
    print("\n======== APLIKASI MANAJEMEN BUKU ========")
    print("1. Tambah Buku ")
    print("2. Tambah Mahasiswa ")
    print("3. Pinjam Buku ")
    print("4. Keluar ")
    pilihan = input("pilih menu (1,2,3,4) : ")

    if pilihan == "1":
        tambahBuku()
    elif pilihan == "2":
        tambahMahasiswa()
    elif pilihan == "3":
        pinjamBuku()
    elif pilihan == "4":
        print("Terimakasih Sudah Menggunakan Aplikasi Ini !!😊")
        break
    else:
        print("Pilihan Tidak Valid. Silahkan Pilih Menu Yang Benar !!!.")