# Mini CRM

Küçük işletmeler için geliştirilmiş, Django tabanlı Müşteri İlişkileri Yönetimi (CRM) sistemi.

## 🚀 Özellikler

- **Müşteri Yönetimi**: Müşterilerinizi ekleyin, düzenleyin ve detaylı bilgilerini saklayın.
- **Satış Fırsatları (Deals)**: Satış süreçlerinizi takip edin (Yeni, İletişimde, Kazanıldı, Kaybedildi).
- **Notlar**: Müşteri görüşmelerinizi ve önemli detayları not alın.
- **Dashboard**: Ana sayfada anlık özet istatistikleri görüntüleyin.
- **Güvenlik**: Her kullanıcı sadece kendi verilerine erişebilir (Data Isolation).

## 🛠 Kullanılan Teknolojiler

- **Backend**: Python, Django 5.x
- **Veritabanı**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Deployment**: WhiteNoise (Statik dosyalar için), Gunicorn

## 📦 Kurulum

Projeyi yerel ortamınızda çalıştırmak için adımları izleyin:

1. **Repoyu klonlayın:**
   ```bash
   git clone https://github.com/isKartal/mini-crm.git
   cd mini-crm
   ```

2. **Sanal ortamı oluşturun ve aktif edin:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **.env dosyasını oluşturun:**
   `.env.example` dosyasını `.env` olarak kopyalayın ve veritabanı bilgilerinizi girin.

5. **Veritabanı göçlerini uygulayın:**
   ```bash
   python manage.py migrate
   ```

6. **Sunucuyu başlatın:**
   ```bash
   python manage.py runserver
   ```

## 🐳 Docker ile Çalıştırma (Önerilen)

Projeyi Docker ile tek komutla ayağa kaldırabilirsiniz:

1. **Docker Compose'u çalıştırın:**
   ```bash
   docker-compose up --build
   ```
2. **Uygulamaya erişin:**
   Tarayıcıda `http://localhost:8000` adresine gidin.

3. **Veri oluşturun (Opsiyonel):**
   ```bash
   docker-compose exec web python manage.py populate_data 50
   ```

### 🛠️ Kolay Kurulum (Makefile)

Komutları ezberlemek zorunda değilsiniz! Proje kök dizininde `Makefile` mevcuttur.

- **Kurulum (Migrate + Seed):** `make setup`
- **Sunucuyu Başlat:** `make up`
- **Yönetici Oluştur:** `make createsuperuser`
- **Veritabanını Sıfırla:** `make down` (Volume silmez)

## 📸 Ekran Görüntüleri

*(Buraya uygulama ekran görüntülerini ekleyebilirsiniz)*

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
