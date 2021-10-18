kendaraan_dan_tarif_list = [
    ["Mobil", 1.0],
    ["Bis", 1.5],
    ["Truk", 2.0]
]

gerbang_tol_list = [
    ["Jakarta", 200],
    ["Tegal", 50],
    ["Semarang", 100],
    ["Jogjakarta", 100],
    ["Surabaya", 200]
]

print("Apa kendaraan yang anda kendarai?")
i = 0
for kendaraan_dan_tarif in kendaraan_dan_tarif_list:
    print(f"{i+1} {kendaraan_dan_tarif[0]}")
    i+=1
print("")
kendaraan_pengguna = int(input(""))-1
print("")

print("Anda memasuki tol dari gerbang mana?")
i = 0
for gerbang_tol in gerbang_tol_list:
    print(f"{i+1} {gerbang_tol[0]}")
    i+=1
print("")
posisi = int(input(""))-1
print("")
 
posisi_penghenti = [0, len(gerbang_tol_list)-1]
 
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
 
tarif = 0
 
if go_left:
    pengubah_posisi = -1
else :
    pengubah_posisi = 1
 
posisi += pengubah_posisi
 
ujung_tol = True
while posisi not in posisi_penghenti:
    print(f"Anda sekarang berada di gerbang tol {gerbang_tol_list[posisi][0]}. Apakah anda akan melanjutkan perjalanan atau keluar di sini? keluar/lanjut")
    keputusan = input().lower()
    print("")
    tarif += gerbang_tol_list[posisi][1]*kendaraan_dan_tarif_list[kendaraan_pengguna][1]
    if keputusan == "keluar":
        ujung_tol = False
        break
    elif keputusan == "lanjut":
        posisi += pengubah_posisi
 
if ujung_tol:
    tarif += gerbang_tol_list[posisi][1]
 
print(f"Anda sekarang telah sampai di kota {gerbang_tol_list[posisi][0]}. Terimakasih telah menggunakan tol Jasamarga. Saldo sebesar {tarif} telah dipotong dari kartu tol anda.")
