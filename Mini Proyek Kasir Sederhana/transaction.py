keranjang = {}

def tambah_ke_keranjang(nama_barang, data_barang, jumlah):
    global keranjang

    #cek stok
    if jumlah > data_barang["stok"]:
        print("Stok tidak mencukupi")
        return False
    
    if nama_barang in keranjang:
        keranjang[nama_barang]["jumlah"] += jumlah
    else:
        keranjang[nama_barang] = {
            "harga" : data_barang["harga"],
            "jumlah" : jumlah
        }

    print(f"{nama_barang} berhasil ditambahkan ke keranjang.")
    return True

def hitung_subtotal():
    total = 0
    for data in keranjang.values():
        total += data["harga"] * data["jumlah"]
    return total

def tampilkan_keranjang():
    print("\n=== Isi Keranjang ===")

    if not keranjang:
        print("Keranjang masih kosong.")
        return

    for nama, data in keranjang.items():
        print(f"{nama} | {data['jumlah']} x {data['harga']}")

    print("Subtotal:", hitung_subtotal())