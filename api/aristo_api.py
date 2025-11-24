"""
ARISTO Kuran Keşif Motoru - Demo Backend API
Flask-based REST API for the Quran discovery engine
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add modules path to system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Sample Quran data (demo purposes)
SAMPLE_VERSES = {
    "1:1": {
        "arabic": "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ",
        "translation": "Rahman ve Rahim olan Allah'ın adıyla",
        "surah": 1,
        "verse": 1
    },
    "2:255": {
        "arabic": "ٱللَّهُ لَآ إِلَـٰهَ إِلَّا هُوَ ٱلْحَىُّ ٱلْقَيُّومُ",
        "translation": "Allah ki, O'ndan başka ilah yoktur. Diridir, Kayyum'dur",
        "surah": 2,
        "verse": 255
    }
}

@app.route('/')
def home():
    """Root endpoint - API info"""
    return jsonify({
        "name": "ARISTO Kuran Keşif Motoru API",
        "version": "1.0.0",
        "description": "Kuran keşif motoru için backend API",
        "endpoints": {
            "/api/search": "POST - Kuran metninde arama",
            "/api/verse/<surah>/<verse>": "GET - Belirli bir ayet getir",
            "/api/modules": "GET - Mevcut modülleri listele",
            "/api/analyze": "POST - Ayet analizini yap"
        }
    })

@app.route('/api/search', methods=['POST'])
def search():
    """Search Quran verses"""
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({"error": "Sorgu parametresi gereklidir"}), 400
    
    # Demo: Return sample results
    results = []
    for verse_id, verse_data in SAMPLE_VERSES.items():
        if (query.lower() in verse_data['translation'].lower() or 
            query.lower() in verse_data['arabic']):
            results.append({
                "id": verse_id,
                **verse_data
            })
    
    return jsonify({
        "query": query,
        "count": len(results),
        "results": results
    })

@app.route('/api/verse/<int:surah>/<int:verse>', methods=['GET'])
def get_verse(surah, verse):
    """Get specific verse by surah and verse number"""
    verse_id = f"{surah}:{verse}"
    
    if verse_id in SAMPLE_VERSES:
        return jsonify({
            "id": verse_id,
            **SAMPLE_VERSES[verse_id]
        })
    
    return jsonify({"error": "Ayet bulunamadı"}), 404

@app.route('/api/modules', methods=['GET'])
def list_modules():
    """List available analysis modules"""
    modules = [
        {"id": "fulltext", "name": "Tam Metin Arama", "description": "Kuran'da tam metin araması"},
        {"id": "ebced", "name": "Ebced Analizi", "description": "Ebced sayısal analizi"},
        {"id": "cifr", "name": "Cifr Hesabı", "description": "Cifr hesaplamaları"},
        {"id": "root", "name": "Kök Analizi", "description": "Arapça kök kelime analizi"},
        {"id": "semantic", "name": "Semantik Analiz", "description": "Anlamsal ilişkiler"},
        {"id": "thematic", "name": "Tematik Bağlantılar", "description": "Tematik bağlantılar"}
    ]
    
    return jsonify({
        "count": len(modules),
        "modules": modules
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze verse with selected modules"""
    data = request.get_json()
    verse_id = data.get('verse_id', '')
    modules = data.get('modules', [])
    
    if not verse_id:
        return jsonify({"error": "verse_id parametresi gereklidir"}), 400
    
    # Demo analysis results
    results = {
        "verse_id": verse_id,
        "verse": SAMPLE_VERSES.get(verse_id, {}),
        "analysis": {}
    }
    
    # Add analysis for each requested module
    for module in modules:
        if module == "fulltext":
            results["analysis"]["fulltext"] = {
                "matches": 5,
                "related_verses": ["1:1", "2:255"]
            }
        elif module == "ebced":
            results["analysis"]["ebced"] = {
                "value": 786,
                "significance": "Bu sayı özel bir öneme sahiptir"
            }
        elif module == "root":
            results["analysis"]["root"] = {
                "roots": ["ر-ح-م", "ا-ل-ه"],
                "related_words": ["rahman", "rahim", "allah"]
            }
    
    return jsonify(results)

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "sağlıklı", "service": "aristo-api"})

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"ARISTO API {port} portunda başlatılıyor...")
    print(f"Debug modu: {debug}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
