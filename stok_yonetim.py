# STOK YÖNETİM SİSTEMİ

import json
import os

# Eğer dosya varsa mevcut verileri oku, yoksa boş bir liste oluştur

if os.path.exists("stok.json"):
    with open("stok.json", "r", encoding="utf-8") as dosya:
        try:
            urunler = json.load(dosya)
        except json.JSONDecodeError:
            urunler = []
else:
    urunler = []

def urun_ekle():
    """Yeni ürün ekleme veya mevcut durumu görüntüleme"""
    urun_adi = input("Ürün adını giriniz (Çıkış için q ya basınız): ")
    if urun_adi.lower() == 'q':
        return False
    
    fiyat = int(input("Fiyat giriniz (Mevcut fiyatı korumak için 0 giriniz): "))
    stok = int(input("Stok adedini giriniz: "))

    urun_bulundu = False

    for urun in urunler:
        if urun_adi.lower() == urun["urun"].lower():
            if fiyat != 0:
                urun["fiyat"] = fiyat
            urun["stok"] += stok
            print("\n Ürün zaten mevcut, güncellendi!")
            urun_bulundu = True
            break
    if not urun_bulundu:
        urunler.append({"urun": urun_adi, "fiyat": fiyat, "stok": stok})

    return True

def urun_sil():
    """Kullanıcıdan ürün adı alarak silme işlemi"""
    urun_silme = input("Silmek istediğiniz ürün adını giriniz: ")

    for urun in urunler:
        if urun_silme.lower() == urun["urun"].lower():
            onay = input(f"'{urun_silme}' ürününü silmek istediğinize emin misiniz? (e/h): ")
            if onay == "e":
                urunler.remove(urun)
                print(f"\n '{urun_silme} ürünü başarıyla silindi!'")
                return True
            else:
                print("\n Silme işlemi iptal edildi.")
                return False
    print("\n Bu ürün stokta bulunmuyor.")
    return False

def urun_ara():
    """Kullanıcıdan ürün adı alarak stok durumunu ve fiyatı gösterme"""
    urun_arama = input("Aramak istediğiniz ürün adını giriniz: ")

    for urun in urunler:
        if urun_arama.lower() == urun["urun"].lower():
            print("\n Ürün bulundu!")
            print(f"Fiyat: {urun["fiyat"]} TL")
            print(f"Stok: {urun["stok"]} adet")

            if urun["stok"] == 0:
                print("Bu ürün tükenmiştir!")
            return True
    print("\n Bu ürün stokta bulunmuyor!")
    return False

# Kullanıcı işlem seçimi

while True:
    print("\n **STOK YÖNETİM SİSTEMİ**")
    print("1- Ürün Ekle / Güncelle")
    print("2- Ürün Sil")
    print("3- Ürün Ara")
    print("4- Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4): ")
    if secim == "1":
        urun_ekle()
    elif secim == "2":
        urun_sil()
    elif secim == "3":
        urun_ara()
    elif secim == "4":
        print("\n Çıkış yapılıyor...")
        break
    else:
        print("\n Geçersiz seçim! Lütfen 1, 2, 3 veya 4 giriniz. ")
# JSON dosyasını güncelle

with open("stok.json", "w", encoding="utf-8") as dosya:
    json.dump(urunler, dosya, ensure_ascii=False, indent=4)

print("\n Veriler JSON dosyasına kaydedildi.")

