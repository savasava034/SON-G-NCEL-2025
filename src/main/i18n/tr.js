/**
 * Turkish (tr) language file for main process
 * This file contains all Turkish translations for MarkText main process (menus)
 * Türkçe dil dosyası - MarkText main process için tüm Türkçe çevirileri içerir (menüler)
 */

module.exports = {
  // Menu translations
  menu: {
    // File menu
    file: {
      label: '&Dosya',
      newTab: 'Yeni Sekme',
      newWindow: 'Yeni Pencere',
      openFile: 'Dosya Aç...',
      openFolder: 'Klasör Aç...',
      openRecent: 'Son Kullanılanlar',
      clearRecentlyUsed: 'Son Kullanılanları Temizle',
      save: 'Kaydet',
      saveAs: 'Farklı Kaydet...',
      autoSave: 'Otomatik Kaydet',
      moveTo: 'Taşı...',
      rename: 'Yeniden Adlandır...',
      import: 'İçe Aktar...',
      export: 'Dışa Aktar',
      exportHtml: 'HTML Olarak Dışa Aktar',
      exportPdf: 'PDF Olarak Dışa Aktar',
      print: 'Yazdır',
      preferences: 'Tercihler...',
      closeTab: 'Sekmeyi Kapat',
      closeWindow: 'Pencereyi Kapat',
      quit: 'Çıkış'
    },
    // Edit menu
    edit: {
      label: '&Düzenle',
      undo: 'Geri Al',
      redo: 'Yinele',
      cut: 'Kes',
      copy: 'Kopyala',
      paste: 'Yapıştır',
      copyAsMarkdown: 'Markdown Olarak Kopyala',
      copyAsHtml: 'HTML Olarak Kopyala',
      pasteAsPlainText: 'Düz Metin Olarak Yapıştır',
      selectAll: 'Tümünü Seç',
      duplicate: 'Çoğalt',
      createParagraph: 'Paragraf Oluştur',
      deleteParagraph: 'Paragrafı Sil',
      find: 'Bul',
      findNext: 'Sonrakini Bul',
      findPrevious: 'Öncekini Bul',
      replace: 'Değiştir',
      findInFolder: 'Klasörde Ara',
      screenshot: 'Ekran Görüntüsü',
      lineEnding: 'Satır Sonu',
      lineEndingCrlf: 'Satır başı ve satır besleme (CRLF)',
      lineEndingLf: 'Satır besleme (LF)'
    },
    // Paragraph menu
    paragraph: {
      label: '&Paragraf',
      heading1: 'Başlık 1',
      heading2: 'Başlık 2',
      heading3: 'Başlık 3',
      heading4: 'Başlık 4',
      heading5: 'Başlık 5',
      heading6: 'Başlık 6',
      promoteHeading: 'Başlığı Yükselt',
      demoteHeading: 'Başlığı Düşür',
      table: 'Tablo',
      codeFences: 'Kod Bloğu',
      quoteBlock: 'Alıntı Bloğu',
      mathBlock: 'Matematik Bloğu',
      htmlBlock: 'HTML Bloğu',
      orderedList: 'Numaralı Liste',
      bulletList: 'Madde İşaretli Liste',
      taskList: 'Görev Listesi',
      looseListItem: 'Gevşek Liste Öğesi',
      paragraph: 'Paragraf',
      horizontalRule: 'Yatay Çizgi',
      frontMatter: 'Ön Bilgi'
    },
    // Format menu
    format: {
      label: 'B&içim',
      bold: 'Kalın',
      italic: 'İtalik',
      underline: 'Altı Çizili',
      superscript: 'Üst Simge',
      subscript: 'Alt Simge',
      highlight: 'Vurgula',
      inlineCode: 'Satır İçi Kod',
      inlineMath: 'Satır İçi Matematik',
      strikethrough: 'Üstü Çizili',
      hyperlink: 'Köprü',
      image: 'Resim',
      clearFormatting: 'Biçimlendirmeyi Temizle'
    },
    // View menu
    view: {
      label: '&Görünüm',
      commandPalette: 'Komut Paleti...',
      sourceCodeMode: 'Kaynak Kodu Modu',
      typewriterMode: 'Daktilo Modu',
      focusMode: 'Odak Modu',
      showSidebar: 'Kenar Çubuğunu Göster',
      showTabBar: 'Sekme Çubuğunu Göster',
      toggleTableOfContents: 'İçindekiler Tablosunu Aç/Kapat',
      reloadImages: 'Resimleri Yeniden Yükle',
      showDeveloperTools: 'Geliştirici Araçlarını Göster',
      reloadWindow: 'Pencereyi Yeniden Yükle'
    },
    // Window menu
    window: {
      label: '&Pencere',
      minimize: 'Simge Durumuna Küçült',
      alwaysOnTop: 'Her Zaman Üstte',
      zoomIn: 'Yakınlaştır',
      zoomOut: 'Uzaklaştır',
      showInFullScreen: 'Tam Ekranda Göster',
      bringAllToFront: 'Hepsini Öne Getir'
    },
    // Theme menu
    theme: {
      label: '&Tema',
      cadmiumLight: 'Kadmiyum Açık',
      dark: 'Koyu',
      graphiteLight: 'Grafit Açık',
      materialDark: 'Materyal Koyu',
      oneDark: 'Tek Koyu',
      ulyssesLight: 'Ulysses Açık'
    },
    // Help menu
    help: {
      label: '&Yardım',
      quickStart: 'Hızlı Başlangıç...',
      markdownReference: 'Markdown Referansı...',
      changelog: 'Değişiklik Günlüğü...',
      donateViaOpenCollective: 'Open Collective ile Bağış Yap...',
      feedbackViaTwitter: 'Twitter ile Geri Bildirim...',
      reportIssue: 'Hata Bildir veya Özellik İste...',
      website: 'Web Sitesi...',
      watchOnGithub: 'GitHub\'da İzle...',
      followUsOnGithub: 'GitHub\'da Takip Et...',
      followUsOnTwitter: 'Twitter\'da Takip Et...',
      license: 'Lisans...',
      checkForUpdates: 'Güncellemeleri Kontrol Et...',
      aboutMarkText: 'MarkText Hakkında...'
    },
    // MarkText menu (macOS only)
    marktext: {
      label: 'MarkText',
      aboutMarkText: 'MarkText Hakkında',
      checkForUpdates: 'Güncellemeleri kontrol et...',
      preferences: 'Tercihler',
      services: 'Hizmetler',
      hideMarkText: 'MarkText\'i Gizle',
      hideOthers: 'Diğerlerini Gizle',
      showAll: 'Tümünü Göster',
      quitMarkText: 'MarkText\'ten Çık'
    },
    // Dock menu (macOS only)
    dock: {
      open: 'Aç...',
      clearRecent: 'Son Kullanılanları Temizle'
    },
    // Preferences Edit menu
    prefEdit: {
      label: 'Düzenle',
      cut: 'Kes',
      copy: 'Kopyala',
      paste: 'Yapıştır',
      selectAll: 'Tümünü Seç'
    }
  }
}
