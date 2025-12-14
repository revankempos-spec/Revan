# Aplikasi Akuntansi Sederhana dalam Python
# Fitur: Input transaksi (debit/kredit), Neraca, Buku Besar, Laporan Laba Rugi

# Struktur data untuk menyimpan akun dan saldo
akun = {
    'Kas': 0,  # Aset
    'Piutang Usaha': 0,  # Aset
    'Persediaan': 0,  # Aset
    'Utang Usaha': 0,  # Liabilitas
    'Modal': 0,  # Ekuitas
    'Pendapatan': 0,  # Pendapatan
    'Beban': 0  # Beban
}

# Buku besar: daftar transaksi per akun
buku_besar = {akun_nama: [] for akun_nama in akun}

# Fungsi untuk input transaksi
def input_transaksi():
    print("Masukkan transaksi (debit/kredit):")
    debit_akun = input("Akun Debit: ")
    kredit_akun = input("Akun Kredit: ")
    jumlah = float(input("Jumlah: "))
    
    if debit_akun in akun and kredit_akun in akun:
        # Update saldo
        akun[debit_akun] += jumlah  # Debit meningkatkan aset/liabilitas/ekuitas/beban
        akun[kredit_akun] -= jumlah  # Kredit menurunkan atau meningkatkan tergantung akun
        
        # Catat di buku besar
        buku_besar[debit_akun].append(f"Debit: {jumlah}")
        buku_besar[kredit_akun].append(f"Kredit: {jumlah}")
        print("Transaksi berhasil dicatat.")
    else:
        print("Akun tidak valid.")

# Fungsi untuk menampilkan Neraca
def tampilkan_neraca():
    aset = akun['Kas'] + akun['Piutang Usaha'] + akun['Persediaan']
    liabilitas = akun['Utang Usaha']
    ekuitas = akun['Modal'] + (akun['Pendapatan'] - akun['Beban'])  # Laba bersih ditambahkan ke ekuitas
    
    print("\n--- NERACA ---")
    print(f"Aset: {aset}")
    print(f"Liabilitas: {liabilitas}")
    print(f"Ekuitas: {ekuitas}")
    print(f"Total: {aset} = {liabilitas + ekuitas}")

# Fungsi untuk menampilkan Buku Besar
def tampilkan_buku_besar():
    print("\n--- BUKU BESAR ---")
    for akun_nama, transaksi in buku_besar.items():
        print(f"Akun: {akun_nama}")
        for t in transaksi:
            print(f"  {t}")
        print(f"Saldo Akhir: {akun[akun_nama]}\n")

# Fungsi untuk menampilkan Laporan Laba Rugi
def tampilkan_laba_rugi():
    pendapatan = akun['Pendapatan']
    beban = akun['Beban']
    laba_bersih = pendapatan - beban
    
    print("\n--- LAPORAN LABA RUGI ---")
    print(f"Pendapatan: {pendapatan}")
    print(f"Beban: {beban}")
    print(f"Laba Bersih: {laba_bersih}")

# Menu utama
def menu():
    while True:
        print("\nPilih opsi:")
        print("1. Input Transaksi")
        print("2. Tampilkan Neraca")
        print("3. Tampilkan Buku Besar")
        print("4. Tampilkan Laporan Laba Rugi")
        print("5. Keluar")
        
        pilihan = input("Pilihan: ")
        
        if pilihan == '1':
            input_transaksi()
        elif pilihan == '2':
            tampilkan_neraca()
        elif pilihan == '3':
            tampilkan_buku_besar()
        elif pilihan == '4':
            tampilkan_laba_rugi()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan aplikasi
if __name__ == "__main__":
    menu()
