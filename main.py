import json
import os
from datetime import datetime

DOSYA_ADI = "veriler.json"

def verileri_yukle():
    if not os.path.exists(DOSYA_ADI):
        return []
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        return json.load(f)

def verileri_kaydet(veriler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(veriler, f, ensure_ascii=False, indent=4)

def deneme_ekle():
    print("\n--- Yeni Deneme Sonucu Ekle ---")
    sinav_adi = input("Sınav Adı (örn: KPSS Genel Deneme 1): ").strip()
    try:
        dogru = int(input("Doğru Sayısı: "))
        yanlis = int(input("Yanlış Sayısı: "))
    except ValueError:
        print("Hata: Lütfen geçerli bir tam sayı girin!")
        return

    net = round(dogru - (yanlis / 4), 2)
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")

    veriler = verileri_yukle()
    veriler.append({
        "sinav_adi": sinav_adi,
        "tarih": tarih,
        "dogru": dogru,
        "yanlis": yanlis,
        "net": net
    })
    verileri_kaydet(veriler)
    print(f"Başarılı! '{sinav_adi}' kaydedildi. Hesaplanan Net: {net}")

def denemeleri_listele():
    print("\n--- Kayıtlı Deneme Sonuçları ---")
    veriler = verileri_yukle()
    if not veriler:
        print("Henüz kayıtlı bir deneme bulunmuyor.")
        return

    print(f"{'No':<4} {'Tarih':<18} {'Sınav Adı':<25} {'D':<5} {'Y':<5} {'Net':<6}")
    print("-" * 68)
    for idx, kayit in enumerate(veriler, start=1):
        print(f"{idx:<4} {kayit['tarih']:<18} {kayit['sinav_adi']:<25} {kayit['dogru']:<5} {kayit['yanlis']:<5} {kayit['net']:<6}")

def main():
    while True:
        print("\n=== SINAV DENEME TAKİP SİSTEMİ ===")
        print("1. Yeni Deneme Sonucu Ekle")
        print("2. Kayıtlı Denemeleri Listele")
        print("0. Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            deneme_ekle()
        elif secim == "2":
            denemeleri_listele()
        elif secim == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
