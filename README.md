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
