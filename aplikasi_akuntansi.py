
# =======================================================
# APLIKASI AKUNTANSI SEDERHANA (Python)
# =======================================================

transaksi = []
akun = {
    "Kas": 0,
    "Piutang": 0,
    "Persediaan": 0,
    "Peralatan": 0,
    "Modal": 0,
    "Utang": 0,
    "Pendapatan": 0,
    "Beban": 0
}

def tambah_transaksi():
    print("\n=== INPUT TRANSAKSI ===")
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    keterangan = input("Keterangan: ")

    print("\nPilih akun:")
    for i, a in enumerate(akun.keys()):
        print(f"{i+1}. {a}")
    idx = int(input("Pilih nomor akun: ")) - 1
    nama_akun = list(akun.keys())[idx]

    jenis = input("Jenis (debit/kredit): ").lower()
    nominal = float(input("Nominal: "))

    transaksi.append({
        "tanggal": tanggal,
        "keterangan": keterangan,
        "akun": nama_akun,
        "jenis": jenis,
        "nominal": nominal
    })

    if jenis == "debit":
        akun[nama_akun] += nominal
    else:
        akun[nama_akun] -= nominal

    print("\nTransaksi berhasil disimpan!\n")


def buku_besar():
    print("\n=== BUKU BESAR ===")
    for a in akun:
        print(f"\n--- {a} ---")
        for tr in transaksi:
            if tr["akun"] == a:
                print(f"{tr['tanggal']} | {tr['keterangan']} | {tr['jenis']} | {tr['nominal']}")
        print(f"Saldo akhir: {akun[a]}")
    print()


def laporan_laba_rugi():
    print("\n=== LAPORAN LABA RUGI ===")
    pendapatan = akun["Pendapatan"]
    beban = akun["Beban"]
    laba = pendapatan - beban

    print(f"Pendapatan : {pendapatan}")
    print(f"Beban      : {beban}")
    print(f"Laba/Rugi  : {laba}\n")


def neraca():
    print("\n=== NERACA ===")
    aset = akun["Kas"] + akun["Piutang"] + akun["Persediaan"] + akun["Peralatan"]
    kewajiban = akun["Utang"]
    ekuitas = akun["Modal"] + (akun["Pendapatan"] - akun["Beban"])

    print(f"Aset       : {aset}")
    print(f"Kewajiban  : {kewajiban}")
    print(f"Ekuitas    : {ekuitas}")
    print(f"Total Neraca: {aset} = {kewajiban + ekuitas}\n")


def menu():
    while True:
        print("=== APLIKASI AKUNTANSI SEDERHANA ===")
        print("1. Input Transaksi")
        print("2. Lihat Buku Besar")
        print("3. Laporan Laba Rugi")
        print("4. Neraca")
        print("5. Exit")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_transaksi()
        elif pilih == "2":
            buku_besar()
        elif pilih == "3":
            laporan_laba_rugi()
        elif pilih == "4":
            neraca()
        elif pilih == "5":
            print("Program selesai.")
            break
        else:
            print("Menu tidak valid!\n")


if __name__ == "__main__":
    menu()
