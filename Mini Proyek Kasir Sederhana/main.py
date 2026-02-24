# main.py

import inventory as inv
import transaction as trx
import payment as pay

def menu_utama():
    while True:
        print("\n===== KASIR TOKO KINTAMANI =====")
        print("1. Lihat Menu")
        print("2. Pesan Makanan")
        print("3. Lihat Keranjang")
        print("4. Bayar & Cetak Struk")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            inv.tampilkan_barang()

        elif pilihan == '2':
            inv.tampilkan_barang()
            # Pake .title() biar misal user ngetik "pizza", otomatis jadi "Pizza"
            nama = input("Masukkan nama menu yang mau dibeli: ").title() 
            
            if nama in inv.inventory:
                try:
                    qty = int(input(f"Berapa banyak {nama} yang dibeli? "))
                    if qty > 0:
                        data_item = inv.inventory[nama]
                        sukses = trx.tambah_ke_keranjang(nama, data_item, qty)
                        
                        if sukses:
                            # Update stok di inventory
                            stok_sisa = data_item["stok"] - qty
                            inv.update_stok(nama, stok_sisa)
                    else:
                        print("Jumlah pesanan harus lebih dari 0!")
                except ValueError:
                    print("Error: Masukkan angka yang bener ya!")
            else:
                print("Menu tidak ditemukan. Cek ejaan huruf besar/kecilnya.")

        elif pilihan == '3':
            trx.tampilkan_keranjang()

        elif pilihan == '4':
            if not trx.keranjang:
                print("Keranjangmu masih kosong, beli makan dulu gih!")
                continue
            
            trx.tampilkan_keranjang()
            subtotal = trx.hitung_subtotal()
            
            # Panggil fungsi hitung total (misal kita kasih diskon 10%)
            total_akhir, potongan, pajak = pay.hitung_total_akhir(subtotal, diskon_persen=10)
            print(f"\nTotal Tagihan (Termasuk Diskon & PPN): Rp{total_akhir:,.0f}")
            
            # Looping sampai uangnya cukup
            while True:
                try:
                    uang = float(input("Masukkan jumlah uang bayar: Rp"))
                    berhasil, info = pay.proses_pembayaran(total_akhir, uang)
                    
                    if berhasil:
                        print("Pembayaran sukses! Mencetak struk...\n")
                        
                        # "Jembatan" konversi data dari Dictionary (trx) ke List (pay)
                        daftar_belanja = []
                        for nama_item, isi in trx.keranjang.items():
                            total_harga_item = isi["jumlah"] * isi["harga"]
                            # Format: [Nama, Jumlah, Harga Satuan, Total Harga Item]
                            daftar_belanja.append([nama_item, isi["jumlah"], isi["harga"], total_harga_item])
                        
                        # Cetak Struk
                        pay.cetak_struk(daftar_belanja, subtotal, potongan, pajak, total_akhir, uang, info)
                        
                        # Kosongkan keranjang setelah bayar beres
                        trx.keranjang.clear()
                        break # Keluar dari menu bayar, balik ke menu utama
                        
                    else:
                        print(f"Uang kurang Rp{info:,.0f}. Ayo tambahin lagi!")
                except ValueError:
                    print("Error: Masukkan nominal uang berupa angka!")

        elif pilihan == '5':
            print("Terima kasih sudah mampir di Toko Kintamani!")
            break
            
        else:
            print("Pilihan menu tidak ada. Coba lagi!")

# Memastikan aplikasi berjalan
if __name__ == "__main__":
    menu_utama()