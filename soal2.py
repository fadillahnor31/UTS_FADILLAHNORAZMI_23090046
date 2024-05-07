def cek_tahun(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))

if cek_tahun(tahun):
    print(f"tahun {tahun} merupakan TAHUN KABISAT")
else:
    print(f"tahun {tahun} merupakan BUKAN TAHUN KABISAT")