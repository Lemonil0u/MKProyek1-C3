# payment.py

# menghitung total yang harus dibayar setelah dipotong diskon dan ditambah pajak
def hitung_total_akhir(subtotal, diskon_persen=0, pajak_persen=11):
    potongan = subtotal*(diskon_persen/100)
    total_setelah_diskon = subtotal - potongan
    pajak = total_setelah_diskon*(pajak_persen/100)
    total_akhir = total_setelah_diskon+pajak

    return total_akhir, potongan, pajak

# buat cek apakah uang cukup dan hitung kembalian
def proses_pembayaran(total_tagihan, uang_dibayar):
    if uang_dibayar < total_tagihan:
        kekurangan = total_tagihan - uang_dibayar
        return False, kekurangan
    else:
        kembalian = uang_dibayar - total_tagihan
        return True, kembalian
    
# tampil struk belanja di terminal
def cetak_struk(daftar_belanja, subtotal, potongan, pajak, total_akhir, bayar, kembalian):
    print("\n" + "-"*30)
    print("       TOKO KINTAMANI")
    print("\n" + "-"*30)

# looping item yang dibeli
for item in daftar_belanja:
    print(f"{item[0]:<15}x{item[1]} Rp{item[3]:>8}")

    print("-"*30)
    print(f"Subtotal            : Rp{subtotal:>8}")
    print(f"Diskon              : Rp{potongan:>8}")
    print(f"PPN (11%)           : Rp{subtotal:>8}")
    print("-"*30)
    print(f"TOTAL AKHIR         : Rp{total_akhir:>8}")
    print(f"Bayar               : Rp{bayar:>8}")
    print(f"Kembali             : Rp{kembali:>8}")
    print("-"*30)
    print("     Terima Kasih Telah Belanja!")
    print("-"*30 + "\n")