import modul as mod



while True :
    print("====TOKO HELM NURIZKY====")
    print("1. Tambah data")
    print("2. Edit Data")
    print("3. Hapus data")
    print("4. Cari data")
    print("5. tampil data")
    print("6. Tampil jumlah data")
    print("7. keluar")
    print("")
    pilihan = int(input("masukan pilihan : "))
    if pilihan == 1 :
        mod.tambah_data()
    elif pilihan == 2 :
        mod.edit_data()
    elif pilihan == 3 :
        mod.hapus_data()
    elif pilihan == 4 :
        mod.cari_data()
    elif pilihan == 5 :
        mod.tampil_data()
    elif pilihan == 6 :
        mod.jumlah_data()
    elif pilihan == 7 :
        print("Ingin keluar program? y/n")
        keluar = str(input("masukan pilihan : "))
        if keluar == "y" :
            print("Program selesai")
        break
    else:
        continue