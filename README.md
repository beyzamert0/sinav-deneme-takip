# Sınav Konu ve Deneme Takip Sistemi

## Problem ve Hedef Kitle
Bu proje; KPSS, ALES veya üniversite sınavlarına hazırlanan öğrencilerin çözdükleri deneme sınavı sonuçlarını ve net değişimlerini dağınık kâğıtlar yerine tek bir merkezden düzenli olarak takip edememe problemini çözmek amacıyla geliştirilmiştir.

## İş Takip Panosu
Proje görevleri, kabul kriterleri ve geliştirme süreci GitHub Projects panosu üzerinden takip edilebilir:
👉 [Sınav Takip Panosu](https://github.com/users/beyzamert0/projects/1/views/1)

## Kurulum ve Çalıştırma Adımları
Uygulama yalnızca Python standart kütüphanelerini (`json`, `os`, `datetime`) kullanır; harici bir paket kurulumu gerektirmez.

1. Depoyu bilgisayarınıza klonlayın:
   `git clone [https://github.com/beyzamert0/sinav-deneme-takip.git](https://github.com/beyzamert0/sinav-deneme-takip.git)`
2. Proje klasörüne gidin:
   `cd sinav-deneme-takip`
3. Uygulamayı çalıştırın (Python 3.x gereklidir):
   `python main.py`

## Tamamlanan Özellikler ve Test Adımları

### 1. Yeni Deneme Sonucu Ekleme ve Net Hesaplama (Issue #1)
* **Test Adımı:** Uygulama menüsünden `1` seçeneğini girin. Sınav adı (ör. `Deneme 1`), doğru sayısı (`40`) ve yanlış sayısı (`4`) bilgilerini girin.
* **Beklenen Sonuç:** Sistem 4 yanlışın 1 doğruyu götürmesi kuralına göre neti `39.0` olarak hesaplar ve veriyi `veriler.json` dosyasına kaydeder.

### 2. Kayıtlı Deneme Sonuçlarını Listeleme (Issue #2)
* **Test Adımı:** En az bir veya iki deneme ekledikten sonra uygulama menüsünden `2` seçeneğini girin.
* **Beklenen Sonuç:** Kayıtlı tüm denemeler sıra numarası, tarih, sınav adı, doğru, yanlış ve net sütunlarıyla tablo formatında ekranda listelenir.
