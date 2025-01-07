# Hikaye Tamamlama Uygulaması

Bu proje, kullanıcıların hikaye başlangıçlarını tamamlamalarına yardımcı olan bir web uygulamasıdır. Flask ve OpenAI API'si kullanılarak geliştirilmiştir.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Özellikler

- Kullanıcıdan alınan hikaye başlangıcını OpenAI API'si ile tamamlar.
- Kullanıcı dostu bir arayüz sunar.
- CORS desteği ile farklı kaynaklardan erişime izin verir.

## Kurulum

### Gereksinimler

- Python 3.11
- Flask
- OpenAI Python Kütüphanesi
- Flask-CORS
- Dotenv

### Adımlar

1. **Depoyu Klonlayın:**

   ```bash
   git clone https://github.com/kullaniciadi/hikaye-tamamlama-araci.git
   cd hikaye-tamamlama-araci
   ```

2. **Sanal Ortamı Oluşturun ve Aktif Edin:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows için: .\venv\Scripts\activate
   ```

3. **Gereksinimleri Yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

4. **.env Dosyasını Yapılandırın:**

   `.env` dosyasını açın ve OpenAI API anahtarınızı ekleyin:

   ```plaintext
   OPENAI_API_KEY=sk-your-api-key
   ```

5. **Uygulamayı Başlatın:**

   ```bash
   python backend/app.py
   ```

6. **Tarayıcıda Açın:**

   Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## Kullanım

- Metin kutusuna hikaye başlangıcınızı yazın.
- "Hikayeyi Tamamla" butonuna tıklayın.
- Tamamlanan hikaye sonuç bölümünde görüntülenecektir.
- ![Uploading Ekran Resmi 2025-01-07 18.31.47.png…]()


## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın. Her türlü katkı ve geri bildirim memnuniyetle karşılanır.

