# ARISTO Data Directory

This directory stores Quran data, including:

- Arabic text
- Translations (multiple languages)
- Tafsir (commentaries)
- Metadata (surah info, revelation context, etc.)

## Data Format

Data should be stored in JSON format for easy processing:

```json
{
  "verse_id": "2:255",
  "surah": 2,
  "ayah": 255,
  "text_arabic": "...",
  "translation_en": "...",
  "translation_tr": "...",
  "themes": ["divine attributes", "protection"],
  "revelation_type": "medinan",
  "juz": 3,
  "page": 42
}
```

## Data Sources

To populate this directory with Quran data, you can use:

1. **Quran.com API**: https://api.quran.com/
2. **Tanzil Project**: http://tanzil.net/
3. **Islamic Network API**: https://alquran.cloud/api

## Adding Data

Place your data files here and update the search module to index them.

Example:
```python
from modules import search

# Load and index data
search_module = search.SearchModule()
search_module.build_index()
```
