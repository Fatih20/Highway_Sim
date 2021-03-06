#Program Simulasi Jalan Tol
#Menyimulasikan cara kerja jalan tol

#KAMUS
# kendaraan_dan_tarif_list, gerbang_tol_list : array of array
# posisi_yang_mungkin, posisi_ujung : array of integer
# saldo : float
# i, kendaraan_pengguna, posisi, pengubah_posisi, tambahan_tarif, tarif_total, gerbang_yang_dilewati : integer
# go_left, go_right : bool
# pemberitahuan_posisi_gerbang_tol, pertanyaan_pilihan_lanjut, keputusan : string


#Algoritma
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

pilihan_gerbang_tol_list = [
    ["Jakarta - Surabaya", 0, False],
    ["Tegal - Jakarta", 1, True],
    ["Tegal - Surabaya", 1, False],
    ["Semarang - Jakarta", 2, True],
    ["Semarang - Surabaya", 2, False],
    ["Jogjakarta - Jakarta", 3, True],
    ["Jogjakarta - Surabaya", 3, False],
    ["Surabaya - Jakarta", 4, True],
]

#Tetapkan posisi mana saja yang mungkin dimiliki oleh pengguna serta posisi yang merupakan ujung tol
posisi_yang_mungkin = [i for i in range(0, len(gerbang_tol_list))]
posisi_ujung = [0, len(gerbang_tol_list)-1]

#Menetapkan saldo kartu tol yang dimiliki pengguna
saldo = 1000.0

#Menanyakan apa kendaraan yang dikendarai pengguna
print("Apa kendaraan yang anda kendarai?")
for i in range(len(kendaraan_dan_tarif_list)):
    print(f"{i+1} {kendaraan_dan_tarif_list[i][0]}")
print("")
kendaraan_pengguna = int(input(""))-1
print("")

#Menanyakan pengguna akan masuk tol dari gerbang yang ada di kota mana
print("Anda memasuki tol dari gerbang mana?")
for i in range(len(pilihan_gerbang_tol_list)):
    print(f"{i+1} {pilihan_gerbang_tol_list[i][0]}")
print("")
gerbang_tol_yang_dipilih = pilihan_gerbang_tol_list[int(input(""))-1]
print("")

posisi = gerbang_tol_yang_dipilih[1]
go_left = gerbang_tol_yang_dipilih[2]

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
    
    if posisi in posisi_ujung or gerbang_yang_dilewati == 1:
        print(f"{pemberitahuan_posisi_gerbang_tol}\n")
        keputusan = "lanjut"
        if gerbang_yang_dilewati != 1:
            keputusan = "keluar"
    else :
        print(f"{pemberitahuan_posisi_gerbang_tol} {pertanyaan_pilihan_lanjut}\n")
        keputusan = input().lower()
        print("")

    if gerbang_yang_dilewati != 1:
        tambahan_tarif = gerbang_tol_list[posisi][1]*kendaraan_dan_tarif_list[kendaraan_pengguna][1]
    else : 
        tambahan_tarif = 0
    tarif_total += tambahan_tarif
    saldo -= tambahan_tarif

    if tambahan_tarif != 0:
        print(f"Saldo sebesar {tambahan_tarif*1000} telah dipotong dari kartu tol anda. Saldo anda sekarang adalah {saldo*1000}.\n")

    if keputusan == "keluar":
        break
    elif keputusan == "lanjut":
        posisi += pengubah_posisi
    gerbang_yang_dilewati += 1
 
print(f"Anda telah keluar dari tol dan sekarang telah sampai di kota {gerbang_tol_list[posisi][0]}. Terimakasih telah menggunakan tol Jasamarga.")
