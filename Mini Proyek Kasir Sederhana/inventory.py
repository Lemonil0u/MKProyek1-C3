inventory = {
    "Pizza": {"harga": 250000.0, "stok": 20},
    "Spaghetti": {"harga": 80000.0, "stok": 20},
    "Tenderloin Steak": {"harga": 60000.0, "stok": 30},
    "Chicken Steak": {"harga": 45000.0, "stok": 30},
    "Cheese Burger": {"harga": 35000.0, "stok": 30},
    "Fried Chicken": {"harga": 30000.0, "stok": 30},
    "French Fries": {"harga": 20000.0, "stok": 30},
}

def tampilkan_barang():
    print("Daftar Menu:")
    for nama, data in inventory.items():
        print(f"{nama} | Harga: {data['harga']} | Stok: {data['stok']}")

def tambah_barang(nama, harga, stok):
    if nama in inventory:
        print("Menu sudah ada.")
    else:
        inventory[nama] = {
            "harga": harga,
            "stok": stok
        }
        print("Menu berhasil ditambahkan.")

def update_stok(nama, stok_baru):
    if nama in inventory:
        inventory[nama]["stok"] = stok_baru
        print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")