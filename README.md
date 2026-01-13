# Django Projemiz - Stajerus

## 📚 Proje Hakkında

**Stajerus**, öğrenci hedefli geliştirilmiş modern bir online öğrenci platformudur. 
Kağıt kalem devrini sona erdirmeyi hedefleyen bu uygulama, öğrencilerin dijital ortamda eğitim süreçlerini yönetmelerini sağlarken,
öğretmenlerin de not paylaşabileceği interaktif bir ortam sunar.

---

## 👥 Proje Ekibi

| Ekip Üyesi | Görev | Katkı |
|------------|-------|-------|
| **Miraç Muhammet Karagülle** | Notlar App Developer | Not yönetimi, sosyal özellikler, beğeni/yorum sistemi |
| **Osman Çimen** | kullanicilar App Developer | Kullanıcı kayıt, giriş, şifre yönetimi |
| **Büşra Çelik** | onlineogr App Developer | Ana proje yapılandırması, arayüz tasarımı |

---
# 📚 Django Stajerus - Modern Online Öğrenci Platformu

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2. 7-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Stajerus** - Geleceğin Eğitimi Bugün Başlıyor!  🎓

*Kağıt kalem devrini sona erdiren, öğrencilerin dijital ortamda eğitim süreçlerini yönetmelerini sağlayan modern bir online platform.*

[Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Ekip](#-proje-ekibi)

</div>

---

## 📖 Proje Hakkında

**Stajerus**, öğrenci hedefli geliştirilmiş modern bir online öğrenci platformudur.  Kağıt kalem devrini sona erdirmeyi hedefleyen bu uygulama, öğrencilerin dijital ortamda eğitim süreçlerini yönetmelerini sağlarken, öğretmenlerin de not paylaşabileceği interaktif bir ortam sunar.

### 🎯 Proje Hedefleri

- ✅ Kağıt-kalem kullanımını minimize etmek
- ✅ Öğrenciler için dijital öğrenme ortamı sağlamak
- ✅ Öğretmenlerin not ve materyallerini kolayca paylaşabilmesi
- ✅ Modern ve kullanıcı dostu bir arayüz sunmak
- ✅ Sosyal öğrenme deneyimi sunmak (beğeni, yorum sistemi)

---

## 🚀 Temel Özellikler

### 👤 Kullanıcı Yönetimi (kullanicilar app)
- **Güvenli Kayıt Sistemi**: Gmail tabanlı kullanıcı kaydı
- **Giriş/Çıkış İşlemleri**: Django authentication sistemi
- **Şifre Sıfırlama**: E-posta ile şifre sıfırlama özelliği
- **Kullanıcı Profilleri**: Her kullanıcı için özel profil yönetimi

### 📝 Not Yönetim Sistemi (Notlar app)

#### Ders Organizasyonu
- **Ders Oluşturma**: Her kullanıcı kendi derslerini oluşturabilir (Matematik, Fizik, Tarih vb.)
- **Ders Bazlı Organizasyon**: Notlar derslere göre kategorize edilir
- **Benzersiz Dersler**: Her kullanıcı için ders isimleri benzersizdir (unique_together constraint)

#### Not Alma ve Düzenleme
- **Zengin Not İçeriği**: Başlık ve içerik alanları ile detaylı not alma
- **Zamanlı Kayıt**: Her not oluşturulma ve güncellenme zamanı ile kaydedilir
- **Not Silme**: Ders bazında toplu not silme özelliği
- **Esnek İçerik**:  İsteğe bağlı başlık ve içerik alanları

#### Paylaşım ve Görünürlük
- **Gizlilik Kontrolü**:  Notlar özel veya herkese açık olabilir (is_public)
- **Herkese Açık Notlar**: Diğer kullanıcıların paylaştığı notlara erişim
- **Ders Bazında Paylaşım**: Aynı dersi alan öğrenciler birbirlerinin notlarını görebilir

### 💬 Sosyal Etkileşim Özellikleri

#### Beğeni Sistemi
- **Beğeni (Like)**: Faydalı notları beğenebilme
- **Beğenmeme (Dislike)**: Notları değerlendirebilme
- **Dinamik Sayaçlar**: Anlık beğeni/beğenmeme sayıları
- **Akıllı Toggle**:  Beğeni ile beğenmeme birbirini iptal eder
- **AJAX Destekli**:  Sayfa yenilemeden anlık güncelleme

#### Yorum Sistemi
- **Not Yorumlama**: Her nota yorum yapabilme
- **Kullanıcı Adı Görüntüleme**: Yorumda kullanıcı bilgisi gösterimi
- **Zaman Damgası**: Her yorum için oluşturulma zamanı
- **AJAX Tabanlı**: Anlık yorum ekleme

### 🔍 Arama ve Keşif
- **Ders Arama**: Herkese açık dersler arasında arama yapabilme
- **API Endpoint**: `/api/search-courses/` ile ders arama
- **Filtreleme**:  Sadece herkese açık notları içeren dersler listelenir

---

## 🛠️ Teknolojiler

### Backend
- **Framework**: Django 5.2.7
- **Dil**: Python 3.x
- **Veritabanı**: SQLite (geliştirme) / PostgreSQL (production için uygun)
- **Authentication**: Django built-in authentication system

### Frontend
- **HTML5**: Semantik ve modern HTML yapısı
- **CSS3**:  Özel stil tasarımları
- **JavaScript**:  AJAX istekleri ve dinamik etkileşimler
- **Bootstrap Icons**: Modern ikonlar

### Güvenlik
- **CSRF Koruması**: Django CSRF middleware
- **Şifre Validasyonu**: Çoklu şifre doğrulama kuralları
- **Login Required**: Decorator ile korunan endpoint'ler
- **Güvenli Şifre Saklama**: Django'nun hash sistemı

---

## 📦 Kurulum

### Gereksinimler
- Python 3.8+
- pip
- virtualenv (önerilir)

### Adım Adım Kurulum

```bash
# 1. Projeyi klonlayın
git clone https://github.com/Muhammedkaragulle/Django-Stajerus.git

# 2. Proje dizinine gidin
cd Django-Stajerus

# 3. Sanal ortam oluşturun
python -m venv venv

# 4. Sanal ortamı aktif edin
# Windows için:
venv\Scripts\activate
# Linux/Mac için:
source venv/bin/activate

# 5. Gerekli paketleri yükleyin
pip install django

# 6. Veritabanı migration'larını yapın
python manage.py makemigrations
python manage.py migrate

# 7. (Opsiyonel) Admin kullanıcısı oluşturun
python manage.py createsuperuser

# 8. Sunucuyu başlatın
python manage.py runserver
```

---

## 📝 Kullanım

### Uygulamaya Erişim
Sunucu başlatıldıktan sonra tarayıcınızda şu adreslere gidin: 

- **Ana Sayfa**: `http://127.0.0.1:8000`
- **Kayıt Ol**: `http://127.0.0.1:8000/kullanici/`
- **Giriş Yap**: `http://127.0.0.1:8000/giris/`
- **Hakkımızda**: `http://127.0.0.1:8000/Hakkimizda/`

### Temel İşlemler

#### 1. Kayıt Olma
- Gmail uzantılı (@gmail.com) bir e-posta adresi ile kayıt olun
- Güçlü bir şifre belirleyin
- Otomatik olarak giriş yapılır

#### 2. Ders Oluşturma
- Giriş yaptıktan sonra "Ders Ekle" butonuna tıklayın
- Ders adını girin (örn:  "Matematik 101")
- Ders otomatik olarak oluşturulur

#### 3. Not Alma
- Bir ders seçin
- "Not Ekle" butonuna tıklayın
- Başlık ve içeriği doldurun
- İsterseniz "Herkese Açık" seçeneğini işaretleyin
- Notu kaydedin

#### 4. Sosyal Etkileşim
- Herkese açık notları görüntüleyin
- Beğenin veya beğenmeyin
- Yorum yapın

#### 5. Not Yönetimi
- Notlarınızı ders bazında görüntüleyin
- Ders bazında notları temizleyin
- Notları düzenleyin

---

## 📁 Proje Yapısı

```
Django-Stajerus/
├── Notlar/                    # Not yönetim uygulaması
│   ├── models.py             # Course, Note, Comment modelleri
│   ├── views.py              # Not CRUD işlemleri ve sosyal özellikler
│   ├── urls.py               # Not app URL yapılandırması
│   └── admin.py              # Admin panel yapılandırması
├── kullanicilar/             # Kullanıcı yönetim uygulaması
│   ├── views.py              # Kayıt, giriş, şifre sıfırlama
│   └── urls.py               # Kullanıcı app URL yapılandırması
├── onlineogr/                # Ana proje dizini
│   ├── settings.py           # Django ayarları
│   ├── urls.py               # Ana URL yapılandırması
│   ├── templates/            # HTML şablonları
│   │   ├── base.html         # Temel şablon
│   │   ├── hakkimizda.html   # Hakkımızda sayfası
│   │   ├── index.html        # Ana sayfa
│   │   ├── kullanici. html    # Kayıt sayfası
│   │   └── giris.html        # Giriş sayfası
│   └── static/               # CSS, JS, resim dosyaları
├── manage.py                 # Django yönetim scripti
└── db.sqlite3               # SQLite veritabanı
```

---

## 🗄️ Veritabanı Modelleri

### Course (Ders)
```python
- user: ForeignKey (Kullanıcı)
- name: CharField (Ders adı)
- created:  DateTimeField (Oluşturulma tarihi)
- Unique constraint: (user, name)
```

### Note (Not)
```python
- user: ForeignKey (Kullanıcı)
- course: ForeignKey (Ders)
- title: CharField (Başlık)
- content: TextField (İçerik)
- is_public: BooleanField (Herkese açık mı?)
- likes: ManyToManyField (Beğenenler)
- dislikes: ManyToManyField (Beğenmeyenler)
- created: DateTimeField (Oluşturulma)
- updated: DateTimeField (Güncellenme)
```

### Comment (Yorum)
```python
- user: ForeignKey (Kullanıcı)
- note: ForeignKey (Not)
- content: TextField (Yorum içeriği)
- created: DateTimeField (Oluşturulma tarihi)
```

---

## 🔌 API Endpoints

### Not İşlemleri
- `GET /` - Ana sayfa (not listesi)
- `POST /` - Ders/not oluşturma
- `GET /public/` - Herkese açık dersler
- `GET /public/<course_name>/` - Belirli derse ait herkese açık notlar

### Sosyal Özellikler
- `POST /note/<note_id>/like/` - Beğeni ekle/kaldır (JSON response)
- `POST /note/<note_id>/dislike/` - Beğenmeme ekle/kaldır (JSON response)
- `POST /note/<note_id>/comment/` - Yorum ekle (JSON response)

### Kullanıcı İşlemleri
- `GET/POST /kullanici/` - Kayıt olma
- `GET/POST /giris/` - Giriş yapma
- `GET /logout/` - Çıkış yapma
- `POST /forgot-password/` - Şifre sıfırlama

### Arama
- `GET /api/search-courses/` - Ders arama



## 🎨 Öne Çıkan Özellikler

### ✨ Kullanıcı Deneyimi
- **Responsive Tasarım**: Mobil uyumlu arayüz
- **Kullanıcı Dostu**:  Sezgisel ve kolay kullanım
- **Hızlı Erişim**: Her yerden erişilebilir platform
- **Türkçe Dil Desteği**: Tam Türkçe arayüz (LANGUAGE_CODE:  'tr-TR')

### 🔒 Güvenlik
- **Email Validasyonu**: Sadece Gmail adresleri kabul edilir
- **Unique Email**:  Her email adresi bir kez kullanılabilir
- **Login Required**: Kritik işlemler için giriş zorunluluğu
- **CSRF Protection**: Form güvenliği

### 📊 Veri Yönetimi
- **Cascade Delete**: Kullanıcı silindiğinde ilgili veriler de silinir
- **SET_NULL**: Ders silindiğinde notlar korunur
- **Auto Timestamps**: Otomatik tarih/saat kayıtları
- **Many-to-Many**: Beğeni ve yorum ilişkileri

### 🚀 Performans
- **AJAX Requests**: Sayfa yenilemesiz etkileşim
- **Efficient Queries**: Optimize edilmiş veritabanı sorguları
- **Lazy Loading**: İhtiyaç duyulan veriler yüklenir

---

## 🔮 Gelecek Planları

- [ ] Dosya yükleme özelliği (PDF, resim, vb.)
- [ ] Gelişmiş arama ve filtreleme
- [ ] Not etiketleme sistemi
- [ ] Bildirim sistemi
- [ ] Mobil uygulama
- [ ] REST API geliştirme
- [ ] Export/Import özellikleri (PDF, Word)
- [ ] Gerçek zamanlı işbirliği
- [ ] Markdown desteği

---

## 🤝 Katkıda Bulunma

Bu proje aktif geliştirme aşamasındadır. Katkılarınızı bekliyoruz! 

### Katkı Süreci
1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. 

---

## 📧 İletişim

Proje ile ilgili sorularınız için ekip üyeleriyle iletişime geçebilirsiniz. 

**GitHub**:  [Muhammedkaragulle](https://github.com/Muhammedkaragulle)

---

## 🙏 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz! 

<div align="center">

**Stajerus** - Geleceğin Eğitimi Bugün Başlıyor!  🎓

*Dijital öğrenme deneyiminizi bir üst seviyeye taşıyın!*

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

</div>
