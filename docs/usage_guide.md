# ARISTO Kuran Keşif Motoru - Detaylı Kullanım Rehberi

## İçindekiler

1. [Giriş](#giriş)
2. [Kurulum Detayları](#kurulum-detayları)
3. [Backend API Referansı](#backend-api-referansı)
4. [Frontend Kullanımı](#frontend-kullanımı)
5. [Modül Geliştirme](#modül-geliştirme)
6. [İleri Seviye Kullanım](#ileri-seviye-kullanım)
7. [Sorun Giderme](#sorun-giderme)
8. [En İyi Pratikler](#en-iyi-pratikler)

---

## Giriş

ARISTO Kuran Keşif Motoru, Kuran ayetlerini araştırmak, analiz etmek ve aralarındaki ilişkileri keşfetmek için tasarlanmış modern bir platformdur. Bu rehber, sistemin tüm özelliklerini detaylı olarak açıklar.

### Sistemin Temel Felsefesi

- **Keşif Odaklı**: Sadece bilinen bilgileri göstermek değil, bilinmeyen bağlantıları ortaya çıkarmak
- **Çok Katmanlı Analiz**: 30+ farklı ilim dalından yararlanma
- **Genişletilebilir Mimari**: Yeni modüller kolayca eklenebilir
- **Modern Teknoloji**: Flask (backend) + React (frontend)

---

## Kurulum Detayları

### Sistem Gereksinimleri

**Minimum:**
- Python 3.8+
- Node.js 16+
- 4GB RAM
- 1GB disk alanı

**Önerilen:**
- Python 3.10+
- Node.js 18+
- 8GB RAM
- 5GB disk alanı (veri setleri için)

### Adım Adım Kurulum

#### 1. Python Ortamı Hazırlama

```bash
# Sanal ortam oluştur (önerilen)
python -m venv venv

# Windows'ta aktifleştirme
venv\Scripts\activate

# Linux/Mac'te aktifleştirme
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt
pip install flask-cors
```

#### 2. Yapılandırma

Backend için environment variables (opsiyonel):

```bash
# Linux/Mac
export PORT=5000
export DEBUG=True

# Windows
set PORT=5000
set DEBUG=True
```

Frontend için `.env` dosyası oluşturun (`ui/.env`):

```
REACT_APP_API_URL=http://localhost:5000
```

#### 3. İlk Çalıştırma Kontrolü

```bash
# Backend'i test et
python api/aristo_api.py

# Başka bir terminalde API'yi kontrol et
curl http://localhost:5000/api/health

# Frontend'i başlat
cd ui
npm start
```

---

## Backend API Referansı

### 1. Ana Bilgi Endpoint'i

**URL:** `GET /`

**Açıklama:** API hakkında genel bilgi ve mevcut endpoint'leri listeler.

**Yanıt:**
```json
{
  "name": "ARISTO Kuran Keşif Motoru API",
  "version": "1.0.0",
  "description": "Backend API for Quran discovery engine",
  "endpoints": {
    "/api/search": "POST - Search Quran text",
    "/api/verse/<surah>/<verse>": "GET - Get specific verse",
    "/api/modules": "GET - List available modules",
    "/api/analyze": "POST - Analyze verse with modules"
  }
}
```

### 2. Arama Endpoint'i

**URL:** `POST /api/search`

**Açıklama:** Kuran ayetlerinde arama yapar.

**İstek Body:**
```json
{
  "query": "Rahman"
}
```

**Parametreler:**
- `query` (string, zorunlu): Aranacak metin (Türkçe veya Arapça)

**Başarılı Yanıt (200):**
```json
{
  "query": "Rahman",
  "count": 2,
  "results": [
    {
      "id": "1:1",
      "arabic": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
      "translation": "Rahman ve Rahim olan Allah'ın adıyla",
      "surah": 1,
      "verse": 1
    }
  ]
}
```

**Hata Yanıtı (400):**
```json
{
  "error": "Query parameter is required"
}
```

**cURL Örneği:**
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Allah"}'
```

### 3. Ayet Getirme Endpoint'i

**URL:** `GET /api/verse/<surah>/<verse>`

**Açıklama:** Belirli bir ayeti getirir.

**Parametreler:**
- `surah` (integer): Sure numarası (1-114)
- `verse` (integer): Ayet numarası

**Örnek İstek:**
```bash
GET http://localhost:5000/api/verse/1/1
```

**Başarılı Yanıt (200):**
```json
{
  "id": "1:1",
  "arabic": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
  "translation": "Rahman ve Rahim olan Allah'ın adıyla",
  "surah": 1,
  "verse": 1
}
```

**Hata Yanıtı (404):**
```json
{
  "error": "Verse not found"
}
```

### 4. Modülleri Listeleme

**URL:** `GET /api/modules`

**Açıklama:** Mevcut analiz modüllerini listeler.

**Başarılı Yanıt (200):**
```json
{
  "count": 6,
  "modules": [
    {
      "id": "fulltext",
      "name": "Tam Metin Arama",
      "description": "Full-text search in Quran"
    },
    {
      "id": "ebced",
      "name": "Ebced Analizi",
      "description": "Abjad numerical analysis"
    },
    {
      "id": "cifr",
      "name": "Cifr Hesabı",
      "description": "Cipher calculations"
    }
  ]
}
```

### 5. Ayet Analizi

**URL:** `POST /api/analyze`

**Açıklama:** Seçili modüllerle ayet analizi yapar.

**İstek Body:**
```json
{
  "verse_id": "1:1",
  "modules": ["fulltext", "ebced", "root"]
}
```

**Parametreler:**
- `verse_id` (string, zorunlu): Analiz edilecek ayet (örn: "1:1")
- `modules` (array, zorunlu): Kullanılacak modül ID'leri

**Başarılı Yanıt (200):**
```json
{
  "verse_id": "1:1",
  "verse": {
    "arabic": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
    "translation": "Rahman ve Rahim olan Allah'ın adıyla",
    "surah": 1,
    "verse": 1
  },
  "analysis": {
    "fulltext": {
      "matches": 5,
      "related_verses": ["1:1", "2:255"]
    },
    "ebced": {
      "value": 786,
      "significance": "This number has special significance"
    },
    "root": {
      "roots": ["ر-ح-م", "ا-ل-ه"],
      "related_words": ["rahman", "rahim", "allah"]
    }
  }
}
```

### 6. Sağlık Kontrolü

**URL:** `GET /api/health`

**Açıklama:** API'nin çalışır durumda olduğunu kontrol eder.

**Başarılı Yanıt (200):**
```json
{
  "status": "healthy",
  "service": "aristo-api"
}
```

---

## Frontend Kullanımı

### Arayüz Bileşenleri

#### 1. Arama Bölümü

- **Arama Kutusu**: Türkçe veya Arapça metin girişi
- **Ara Butonu**: Aramayı başlatır
- **Yükleniyor Durumu**: Arama sırasında spinner gösterir

#### 2. Modül Seçimi

- Her modül için checkbox
- Çoklu seçim yapılabilir
- Seçilen modüller analiz için kullanılır

#### 3. Sonuç Kartları

- Ayet bilgisi (Sure ve Ayet numarası)
- Arapça metin (sağdan sola)
- Türkçe çeviri
- Analiz Et butonu

#### 4. Durum Göstergeleri

- API Bağlantı Durumu (yeşil: bağlı, kırmızı: bağlantı yok)
- Hata mesajları
- Başarı bildirimleri

### Kullanım Senaryoları

#### Senaryo 1: Basit Arama

1. Arama kutusuna "Rahman" yazın
2. "Ara" butonuna tıklayın
3. Sonuçları görüntüleyin

#### Senaryo 2: Modül ile Analiz

1. Arama yapın veya bir ayet bulun
2. Analiz modüllerinden birini veya birkaçını seçin
3. Sonuç kartında "Analiz Et" butonuna tıklayın
4. Konsolu açarak detaylı analiz sonuçlarını görün (F12)

#### Senaryo 3: Arapça Arama

1. Arapça metin girin: "الله"
2. Arama yapın
3. İlgili ayetleri görüntüleyin

---

## Modül Geliştirme

### Yeni Modül Oluşturma

#### 1. Modül Dosyası Oluşturma

`modules/` dizininde yeni bir Python dosyası oluşturun:

```python
# modules/ebced_module.py

class EbcedModule:
    """
    Ebced (Abjad) sayısal analiz modülü
    Her Arap harfine sayısal değer atar ve hesaplamalar yapar
    """
    
    def __init__(self):
        # Ebced değerleri
        self.ebced_values = {
            'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1,
            'ب': 2, 'ج': 3, 'د': 4, 'ه': 5,
            'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
            'ي': 10, 'ى': 10, 'ئ': 10,
            'ك': 20, 'ل': 30, 'م': 40, 'ن': 50,
            'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
            'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400,
            'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800,
            'ظ': 900, 'غ': 1000
        }
    
    def calculate(self, text):
        """
        Metnin Ebced değerini hesapla
        
        Args:
            text: Arapça metin
            
        Returns:
            Dictionary with calculation results
        """
        total = 0
        letter_values = []
        
        for char in text:
            if char in self.ebced_values:
                value = self.ebced_values[char]
                total += value
                letter_values.append({
                    'letter': char,
                    'value': value
                })
        
        return {
            'total': total,
            'letter_count': len(letter_values),
            'letter_values': letter_values,
            'average': total / len(letter_values) if letter_values else 0
        }
    
    def analyze_verse(self, verse_data):
        """
        Ayet için tam analiz yap
        
        Args:
            verse_data: Ayet verisi (arabic text içermeli)
            
        Returns:
            Analiz sonuçları
        """
        arabic_text = verse_data.get('arabic', '')
        calculation = self.calculate(arabic_text)
        
        return {
            'ebced_value': calculation['total'],
            'letter_count': calculation['letter_count'],
            'average_value': calculation['average'],
            'details': calculation['letter_values'],
            'interpretation': self._interpret(calculation['total'])
        }
    
    def _interpret(self, value):
        """
        Ebced değerinin yorumu
        """
        if value == 786:
            return "Bu değer 'Bismillah'in Ebced değeridir"
        elif value == 66:
            return "Bu değer 'Allah' kelimesinin Ebced değeridir"
        else:
            return f"Ebced değeri: {value}"


# Test kodu
if __name__ == "__main__":
    module = EbcedModule()
    
    # Test
    result = module.calculate("بسم الله")
    print(f"Ebced değeri: {result['total']}")
    print(f"Harf sayısı: {result['letter_count']}")
```

#### 2. API'ye Modül Ekleme

`api/aristo_api.py` dosyasını güncelleyin:

```python
# Import the new module
from modules.ebced_module import EbcedModule

# Initialize module
ebced_module = EbcedModule()

# Update modules list endpoint
@app.route('/api/modules', methods=['GET'])
def list_modules():
    modules = [
        # ... existing modules ...
        {
            "id": "ebced", 
            "name": "Ebced Analizi", 
            "description": "Abjad numerical analysis"
        }
    ]
    return jsonify({"count": len(modules), "modules": modules})

# Update analyze endpoint to use the module
@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    verse_id = data.get('verse_id', '')
    modules = data.get('modules', [])
    
    verse_data = SAMPLE_VERSES.get(verse_id, {})
    results = {
        "verse_id": verse_id,
        "verse": verse_data,
        "analysis": {}
    }
    
    # Use the new module
    if "ebced" in modules:
        results["analysis"]["ebced"] = ebced_module.analyze_verse(verse_data)
    
    return jsonify(results)
```

### Modül Geliştirme En İyi Pratikleri

1. **Temiz Arayüz**: Her modül `analyze_verse()` methodu içermeli
2. **Hata Yönetimi**: Try-catch blokları kullanın
3. **Dokümantasyon**: Docstring'ler ekleyin
4. **Test Edilebilirlik**: `if __name__ == "__main__"` ile test kodu ekleyin
5. **Performans**: Büyük veri setleri için optimizasyon yapın

---

## İleri Seviye Kullanım

### 1. Veritabanı Entegrasyonu

Gerçek bir Kuran veritabanı eklemek için:

```python
import sqlite3

class QuranDatabase:
    def __init__(self, db_path="quran.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def get_verse(self, surah, verse):
        query = """
            SELECT surah, verse, arabic, translation 
            FROM verses 
            WHERE surah = ? AND verse = ?
        """
        self.cursor.execute(query, (surah, verse))
        return self.cursor.fetchone()
    
    def search(self, query):
        query_sql = """
            SELECT surah, verse, arabic, translation 
            FROM verses 
            WHERE arabic LIKE ? OR translation LIKE ?
            LIMIT 100
        """
        pattern = f"%{query}%"
        self.cursor.execute(query_sql, (pattern, pattern))
        return self.cursor.fetchall()
```

### 2. Caching Mekanizması

Redis ile caching:

```python
import redis
import json

cache = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    
    # Check cache
    cache_key = f"search:{query}"
    cached = cache.get(cache_key)
    
    if cached:
        return jsonify(json.loads(cached))
    
    # Perform search
    results = perform_search(query)
    
    # Cache results (expire in 1 hour)
    cache.setex(cache_key, 3600, json.dumps(results))
    
    return jsonify(results)
```

### 3. Async İşlemler

Uzun süren analizler için:

```python
from flask import Flask
import asyncio

@app.route('/api/analyze-async', methods=['POST'])
async def analyze_async():
    data = request.get_json()
    
    # Start async analysis
    task_id = start_analysis_task(data)
    
    return jsonify({
        "task_id": task_id,
        "status": "processing",
        "check_url": f"/api/task/{task_id}"
    })

@app.route('/api/task/<task_id>')
def check_task(task_id):
    result = get_task_result(task_id)
    return jsonify(result)
```

---

## Sorun Giderme

### Backend Sorunları

#### Problem: "ModuleNotFoundError: No module named 'flask'"
**Çözüm:**
```bash
pip install flask flask-cors
```

#### Problem: "Address already in use"
**Çözüm:**
```bash
# Port kullanımını kontrol et
lsof -i :5000  # Mac/Linux
netstat -ano | findstr :5000  # Windows

# Portu değiştir
PORT=5001 python api/aristo_api.py
```

#### Problem: CORS hatası
**Çözüm:**
```bash
pip install flask-cors
```

API dosyasında:
```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

### Frontend Sorunları

#### Problem: "npm: command not found"
**Çözüm:**
Node.js'i kurun: https://nodejs.org/

#### Problem: "Cannot connect to backend"
**Çözüm:**
1. Backend'in çalıştığından emin olun
2. `.env` dosyasını kontrol edin
3. Proxy ayarlarını kontrol edin (`ui/package.json`)

#### Problem: Port 3000 kullanımda
**Çözüm:**
```bash
PORT=3001 npm start
```

---

## En İyi Pratikler

### Güvenlik

1. **API Keys**: Hassas bilgileri environment variables'da tutun
2. **CORS**: Production'da belirli domain'lere izin verin
3. **Rate Limiting**: API'ye rate limiting ekleyin
4. **Validation**: Tüm inputları validate edin

### Performans

1. **Caching**: Sık kullanılan sorguları cache'leyin
2. **Database Indexing**: Arama alanlarını indexleyin
3. **Pagination**: Büyük sonuç setlerini sayfalandırın
4. **Lazy Loading**: Frontend'de lazy loading kullanın

### Kod Kalitesi

1. **Linting**: Python için `pylint`, JavaScript için `eslint` kullanın
2. **Formatting**: `black` (Python) ve `prettier` (JavaScript)
3. **Testing**: Unit testler yazın
4. **Documentation**: Kod dokümantasyonu ekleyin

---

## Örnek Projeler

### Proje 1: Tefsir Modülü

Ayetlere tefsir eklemek için:

```python
# modules/tafsir_module.py

class TafsirModule:
    def __init__(self):
        self.tafsir_data = self.load_tafsir()
    
    def load_tafsir(self):
        # Tefsir verisini yükle
        return {}
    
    def get_tafsir(self, verse_id):
        return self.tafsir_data.get(verse_id, {})
```

### Proje 2: Tema Analizi

Ayetlerdeki temaları bulma:

```python
# modules/theme_module.py

class ThemeModule:
    def __init__(self):
        self.themes = {
            'rahmet': ['rahman', 'rahim', 'merhamet'],
            'yaratılış': ['halk', 'yaratmak', 'yaratıcı'],
            'adalet': ['adil', 'hak', 'adalet']
        }
    
    def identify_themes(self, text):
        found_themes = []
        for theme, keywords in self.themes.items():
            for keyword in keywords:
                if keyword in text.lower():
                    found_themes.append(theme)
                    break
        return found_themes
```

---

## Kaynaklar

### API Dokümantasyonu
- Flask: https://flask.palletsprojects.com/
- Flask-CORS: https://flask-cors.readthedocs.io/

### Frontend Dokümantasyonu
- React: https://react.dev/
- React Bootstrap: https://react-bootstrap.github.io/
- Axios: https://axios-http.com/

### Kuran Kaynakları
- Kuran API: https://alquran.cloud/api
- Tanzil Project: http://tanzil.net/

### Geliştirici Araçları
- Postman: API test için
- React DevTools: React debugging için
- Python Debugger: pdb

---

## Sıkça Sorulan Sorular

**S: Gerçek Kuran verisini nasıl eklerim?**
A: SQLite veritabanı kullanarak tüm ayetleri saklayabilirsiniz. Tanzil.net'ten veri indirebilirsiniz.

**S: Yeni bir dil desteği nasıl eklerim?**
A: Veritabanına yeni dil çevirilerini ekleyin ve API'de dil parametresi ekleyin.

**S: Modüller arası iletişim nasıl sağlanır?**
A: Modül sonuçlarını bir dictionary'de toplayıp, diğer modüllere input olarak verebilirsiniz.

**S: Production deployment nasıl yapılır?**
A: Gunicorn (backend) ve Nginx (frontend) kullanarak deploy edebilirsiniz. Docker da kullanılabilir.

---

## Güncellemeler ve Değişiklik Notları

### v1.0.0 (İlk Sürüm)
- Temel backend API
- React frontend
- Tam metin arama modülü
- Demo verileri

### Planlanan Özellikler
- [ ] Tam Kuran veritabanı entegrasyonu
- [ ] Daha fazla analiz modülü
- [ ] Kullanıcı hesapları
- [ ] Arama geçmişi
- [ ] Export özellikleri (PDF, JSON)
- [ ] Mobil uygulama

---

**Son Güncelleme:** 2025-11-23

Bu rehber sürekli güncellenecektir. Katkılarınızı GitHub üzerinden yapabilirsiniz.
