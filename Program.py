#Menginisialisasi jenis-jenis kendaraan yang ada dan berapa kali tarif normal yang harus mereka bayar
kendaraan_dan_tarif_list = [
    ["Mobil", 1.0],
    ["Bis", 1.5],
    ["Truk", 2.0]
]

#Menginisialisasi gerbang tol yang ada beserta tarifnya
gerbang_tol_list = [
    ["Jakarta", 200],
    ["Tegal", 50],
    ["Semarang", 100],
    ["Jogjakarta", 100],
    ["Surabaya", 200]
]

#Tetapkan posisi mana saja yang mungkin dimiliki oleh pengguna
posisi_yang_mungkin = [i for i in range(0, len(gerbang_tol_list))]
posisi_ujung = [0, len(gerbang_tol_list)-1]

#Menanyakan apa kendaraan yang dikendarai pengguna
print("Apa kendaraan yang anda kendarai?")
i = 0
for kendaraan_dan_tarif in kendaraan_dan_tarif_list:
    print(f"{i+1} {kendaraan_dan_tarif[0]}")
    i+=1
print("")
kendaraan_pengguna = int(input(""))-1
print("")

#Menanyakan pengguna akan masuk tol dari gerbang yang ada di kota mana
print("Anda memasuki tol dari gerbang mana?")
i = 0
for gerbang_tol in gerbang_tol_list:
    print(f"{i+1} {gerbang_tol[0]}")
    i+=1
print("")
posisi = int(input(""))-1
print("")

#Menetapkan apakah pengguna akan melakukan perjalanan ke barat atau timur
if posisi == len(gerbang_tol_list)-1:
    go_left = True
elif posisi == 0:
    go_left = False
else :
    arah = input("Mau ke arah Timur atau Barat? ").lower()
    print("")
    if arah == "timur":
        go_left = False
    elif arah == "barat":
        go_left = True

if go_left:
    pengubah_posisi = -1
else :
    pengubah_posisi = 1
 
tarif_total = 0
gerbang_yang_dilewati = 1

#Perjalanan selanjutnya akan mengikuti input pengguna
while posisi in posisi_yang_mungkin:
    pemberitahuan_posisi_gerbang_tol = f"Anda telah memasuki gerbang tol {gerbang_tol_list[posisi][0]}."
    pertanyaan_pilihan_lanjut = "Apakah anda akan melanjutkan perjalanan atau keluar di sini? keluar/lanjut"
    
    if posisi in posisi_ujung:
        print(f"{pemberitahuan_posisi_gerbang_tol}")
        keputusan = "lanjut"
        if gerbang_yang_dilewati != 1:
            keputusan = "keluar"
    else :
        print(f"{pemberitahuan_posisi_gerbang_tol} {pertanyaan_pilihan_lanjut}")
        keputusan = input().lower()
        print("")

    tambahan_tarif = gerbang_tol_list[posisi][1]*kendaraan_dan_tarif_list[kendaraan_pengguna][1]
    tarif_total += tambahan_tarif

    if keputusan == "keluar":
        break
    elif keputusan == "lanjut":
        posisi += pengubah_posisi
    gerbang_yang_dilewati += 1
 
print(f"Anda telah keluar dari tol dan sekarang telah sampai di kota {gerbang_tol_list[posisi][0]}. Terimakasih telah menggunakan tol Jasamarga. Saldo sebesar {tarif_total} telah dipotong dari kartu tol anda.")
