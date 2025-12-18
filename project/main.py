    # Menambahkan Library Pandas

import pandas as pd

    # Data Unsur Periodik
    
data = {
        "Simbol": [
            "H","He","Li","Be","B","C","N","O","F","Ne",
            "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
            "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
            "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
            "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
            "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
            "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
            "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
            "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
            "Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
            "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",
            "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
        ],

        "Nama": [
            "Hidrogen","Helium","Litium","Berilium","Boron","Karbon","Nitrogen","Oksigen","Fluorin","Neon",
            "Natrium","Magnesium","Aluminium","Silikon","Fosfor","Belerang","Klorin","Argon","Kalium","Kalsium",
            "Skandium","Titanium","Vanadium","Kromium","Mangan","Besi","Kobalt","Nikel","Tembaga","Seng",
            "Galium","Germanium","Arsen","Selenium","Br om","Kripton","Rubidium","Stronsium","Yttrium","Zirkonium",
            "Niobium","Molibdenum","Teknesium","Rutenium","Rodium","Paladium","Perak","Kadmium","Indium","Timah",
            "Antimon","Telurium","Iodin","Xenon","Sesium","Barium","Lantanum","Serium","Praseodimium","Neodimium",
            "Prometium","Samarium","Europium","Gadolinium","Terbium","Disprosium","Holmium","Erbium","Tuliu","Iterbium",
            "Lutesium","Hafnium","Tantalum","Wolfram","Renium","Osmium","Iridium","Platina","Emas","Raksa",
            "Talium","Timbal","Bismut","Polonium","Astatin","Radon","Fransium","Radium","Aktinium","Toriun",
            "Protaktinium","Uranium","Neptunium","Plutonium","Amerisium","Kuriun","Berkelium","Kalifornium","Einsteinium","Fermium",
            "Mendelevium","Nobelium","Lawrensium","Ruterfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium",
            "Roentgenium","Kopernisium","Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Oganesson"
        ],

        "Nomor_Atom": list(range(1, 119))
    }

tabel = pd.DataFrame(data)


    # Kode Fungsi Untuk Menu Utama
    # Fungsi Menampilkan Semua Tabel
    
def tampilkan_semua():
    print ("\n========== DAFTAR UNSUR ==========")
    print (tabel.to_string(index=False))
    print ("===================================")
    
    # Fungsi Mencari Unsur Dengan Simbol
    
def cari_dengan_simbol():
    simbol = input ("Masukkan Simbol: ").capitalize()
    hasil = tabel[tabel["Simbol"]==simbol]
    if hasil.empty:
        print ("Tidak Ditemukan!")
    else:
        print (hasil.to_string(index=False))
        
    # Fungsi Mencari Unsur Dengan Nama
    
def cari_dengan_nama():
    nama = input("Masukkan Nama Unsur: ").capitalize()
    hasil = tabel[tabel["Nama"]==nama]
    if hasil.empty:
        print ("Tidak Ditemukan!")
    else:
        print (hasil.to_string(index=False))
    
    # Fungsi Mencari Unsur Dengan Nomor
    
def cari_dengan_nomor():

    nomor = int(input("Masukkan Nomor Atom: "))
    hasil = tabel[tabel["Nomor_Atom"]==nomor]
    if hasil.empty:
        print ("Tidak Ditemukan!")
    else:
        print (hasil.to_string(index=False))
    # Fungsi Menambahkan Unsur
    
def tambah_data():
    global tabel
    simbol = input ("Masukkan Simbol Yang Ingin di Tambah: ").capitalize()
    nama = input ("Masukkan Nama Yang Ingin di Tambah: ").capitalize()
    nomor_atom = int(input("Masukkan Nomor Atom Yang ingin di Tambah: "))
    tambahan_data = {
        "Simbol": simbol,
        "Nama": nama,
        "Nomor_Atom": nomor_atom
    }
    
    tabel = pd.concat ([tabel, pd.DataFrame([tambahan_data])], ignore_index=True)
    print ("Data Berhasil Ditambahkan")
    
    # Fungsi Hapus Unsur
    
def hapus_data():
    global tabel
    simbol = input("Masukkan Simbol Yang Ingin di Hapus: ").capitalize()
    if simbol not in tabel["Simbol"].values:
        print("Data Tidak Ditemukan!")
        return
    tabel = tabel[tabel["Simbol"] != simbol]
    print("Data Berhasil Dihapus!")
    
    # Program Utama

def menu():
    print ("""
                                                                         
  ▄▄▄▄   ▄▄▄      ▄▄                                               ▄▄▄▄  
 █▀ ██  ██         ██                                            ▄██▀▀▀█ 
    ██ ██          ██       ▄                    ▄▄              ██      
    █████    ▄█▀█▄ ██ ▄███▄ ███▄███▄ ████▄ ▄███▄ ██ ▄█▀          ██▄███▄ 
    ██ ██▄   ██▄█▀ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ████     ▀▀▀▀   ██▀  ██ 
  ▀██▀  ▀██▄▄▀█▄▄▄▄██▄▀███▀▄██ ██ ▀█▄████▀▄▀███▀▄██ ▀█▄          ▀█████▀ 
                                     ██                                  
                                     ▀                                   """)
    while True:
        print("""
====== MINI TABEL PERIODIK ======

1. Tampilkan Tabel
2. Cari Berdasarkan Simbol
3. Cari Berdasarkan Nama 
4. Cari Berdasarkan Nomor Atom
5. Tambah Data Baru
6. Hapus Data
7. Keluar Program
""")
        pilih = input("Pilih Menu [1-7]: ")
        if pilih == "1":
            tampilkan_semua()
        elif pilih == "2":
            cari_dengan_simbol()
        elif pilih == "3":
            cari_dengan_nama()
        elif pilih == "4":
            cari_dengan_nomor()
        elif pilih == "5":
            tambah_data()
        elif pilih == "6":
            hapus_data()
        elif pilih == "7":
            print("TERIMAKASIH SUDAH MENGGUNAKAN PROGRAM INI")
            print("")
            break
        else:
            print("Pilihan Tidak Tersedia! / Input Salah")
menu()
