# ARISTO Kuran Keşif Motoru

Kuran ayetlerini aramak, analiz etmek ve keşfetmek için gelişmiş araştırma platformu.

## 📋 Genel Bakış

ARISTO, Kuran ayetlerini merkez alan, 30+ ilim modülünü aynı anda işletebilen, dış ansiklopedik ve akademik kaynaklardan veri çekebilen, her sorguda hem görünen hem görünmeyen bağlantıları keşfedip ortaya çıkaran, çok katmanlı, çok yönlü bir keşif motoru ve araştırma sistemidir.

### Özellikler

- 🔍 **Tam Metin Arama**: Türkçe ve Arapça metin araması
- 📊 **Çoklu Analiz Modülleri**: Ebced, Cifr, Kök Analizi, Semantik, Tematik bağlantılar
- 🌐 **RESTful API**: Flask tabanlı backend
- 💻 **Modern Web Arayüzü**: React tabanlı kullanıcı dostu arayüz
- 📚 **Genişletilebilir Modül Sistemi**: Yeni analiz modülleri kolayca eklenebilir

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- Node.js 16 veya üzeri
- npm veya yarn

### 1. Depoyu Klonlama

```bash
git clone https://github.com/savasava034/SON-G-NCEL-2025.git
cd SON-G-NCEL-2025
```

### 2. Backend Kurulumu

```bash
# Python bağımlılıklarını yükle
pip install -r requirements.txt

# CORS desteği için flask-cors yükle (gerekiyorsa)
pip install flask-cors
```

### 3. Frontend Kurulumu

```bash
# UI dizinine git
cd ui

# Bağımlılıkları yükle
npm install

# Ana dizine dön
cd ..
```

## 🎯 Uygulamayı Başlatma

### Backend API'yi Başlatma

```bash
# Ana dizinde
python api/aristo_api.py
```

Backend varsayılan olarak `http://localhost:5000` adresinde çalışır.

API durumunu kontrol etmek için:
```bash
curl http://localhost:5000/
```

### Frontend'i Başlatma

Yeni bir terminal açın:

```bash
cd ui
npm start
```

Frontend `http://localhost:3000` adresinde açılır ve tarayıcınızda otomatik olarak yüklenecektir.

## 📖 API Kullanımı

### Endpoints

#### 1. Ana Bilgi
```
GET /
```

#### 2. Arama
```
POST /api/search
Content-Type: application/json

{
  "query": "Rahman"
}
```

#### 3. Belirli Ayet Getirme
```
GET /api/verse/<surah>/<verse>
```
Örnek: `/api/verse/1/1`

#### 4. Modülleri Listeleme
```
GET /api/modules
```

#### 5. Ayet Analizi
```
POST /api/analyze
Content-Type: application/json

{
  "verse_id": "1:1",
  "modules": ["fulltext", "ebced", "root"]
}
```

#### 6. Sağlık Kontrolü
```
GET /api/health
```

## 🔧 Modül Sistemi

### Mevcut Modüller

1. **Tam Metin Arama** (`fulltext_search.py`)
   - Türkçe ve Arapça metin araması
   - İndeksleme ve hızlı arama
   - Kelime tokenizasyonu

### Yeni Modül Ekleme

`modules/` dizininde yeni bir Python dosyası oluşturun:

```python
# modules/yeni_modul.py

class YeniModul:
    def __init__(self):
        # Başlangıç ayarları
        pass
    
    def analyze(self, verse_data):
        # Analiz mantığı
        return {
            "result": "analiz sonucu"
        }
```

Ardından API'de modülü kaydedin ve kullanıma açın.

## 📚 Örnek Kullanım

### Python'dan API Kullanımı

```python
import requests

# Arama yap
response = requests.post('http://localhost:5000/api/search', 
                        json={'query': 'Allah'})
print(response.json())

# Belirli ayeti getir
response = requests.get('http://localhost:5000/api/verse/1/1')
print(response.json())
```

### JavaScript'ten API Kullanımı

```javascript
// Arama yap
fetch('http://localhost:5000/api/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: 'Rahman' })
})
.then(res => res.json())
.then(data => console.log(data));
```

## 🐳 Docker ile Çalıştırma (Opsiyonel)

Docker kullanarak uygulamayı çalıştırmak için:

```bash
# Backend için
docker build -t aristo-backend -f Dockerfile.backend .
docker run -p 5000:5000 aristo-backend

# Frontend için
docker build -t aristo-frontend -f Dockerfile.frontend ./ui
docker run -p 3000:3000 aristo-frontend
```

## 📁 Proje Yapısı

```
SON-G-NCEL-2025/
├── api/
│   └── aristo_api.py          # Flask backend API
├── modules/
│   └── fulltext_search.py     # Tam metin arama modülü
├── ui/
│   ├── public/
│   │   └── index.html         # HTML template
│   ├── src/
│   │   ├── App.js             # Ana React bileşeni
│   │   ├── index.js           # React entry point
│   │   └── index.css          # Stiller
│   └── package.json           # Frontend bağımlılıkları
├── docs/
│   └── usage_guide.md         # Detaylı kullanım rehberi
├── requirements.txt           # Python bağımlılıkları
└── README.md                  # Bu dosya
```

## 🧪 Test Etme

### Backend Testleri

```bash
# Manuel test
python api/aristo_api.py

# Başka bir terminalde
curl http://localhost:5000/api/health
```

### Modül Testleri

```bash
# Tam metin arama modülünü test et
python modules/fulltext_search.py
```

## 🛠️ Geliştirme

### Backend Geliştirme

1. `api/aristo_api.py` dosyasında yeni endpoint'ler ekleyin
2. `modules/` dizininde yeni analiz modülleri oluşturun
3. API'yi test edin

### Frontend Geliştirme

1. `ui/src/` dizininde React bileşenlerini düzenleyin
2. Bootstrap bileşenlerini kullanarak UI geliştirin
3. `npm start` ile değişiklikleri canlı görün

## 📖 Daha Fazla Bilgi

Detaylı kullanım ve modül geliştirme rehberi için:
- [Kullanım Rehberi](docs/usage_guide.md)
- [Mimari Dokümantasyon](Kuran_Kesif_Motoru_Mimari_Tasarim_v2_CPU_API.md)

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje eğitim ve araştırma amaçlıdır.

## 📞 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**Not**: Bu proje demo amaçlıdır. Gerçek bir üretim ortamında kullanmadan önce güvenlik ve performans optimizasyonları yapılmalıdır.
