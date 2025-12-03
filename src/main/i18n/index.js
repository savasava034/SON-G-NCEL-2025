/**
 * Internationalization (i18n) module for main process
 * Handles language loading and translation for menus
 */

const en = require('./en')
const tr = require('./tr')

// Available languages
const languages = {
  en: en,
  tr: tr
}

// Default language
const DEFAULT_LANGUAGE = 'tr'

// Current language
let currentLanguage = DEFAULT_LANGUAGE

/**
 * Get current language
 * @returns {string} Current language code
 */
function getCurrentLanguage () {
  return currentLanguage
}

/**
 * Set current language
 * @param {string} lang Language code (e.g., 'en', 'tr')
 */
function setLanguage (lang) {
  if (languages[lang]) {
    currentLanguage = lang
  } else {
    console.warn(`Language "${lang}" not found, using default language "${DEFAULT_LANGUAGE}"`)
    currentLanguage = DEFAULT_LANGUAGE
  }
}

/**
 * Get translation by key path
 * @param {string} keyPath Dot-separated key path (e.g., 'menu.file.save')
 * @param {string} lang Optional language code, defaults to current language
 * @returns {string|object} Translation value or object
 */
function t (keyPath, lang = null) {
  const langCode = lang || currentLanguage
  const translations = languages[langCode] || languages[DEFAULT_LANGUAGE]

  const keys = keyPath.split('.')
  let value = translations

  for (const key of keys) {
    if (value && typeof value === 'object' && key in value) {
      value = value[key]
    } else {
      console.warn(`Translation key "${keyPath}" not found in language "${langCode}"`)
      return keyPath
    }
  }

  return value
}

/**
 * Get all translations for current language
 * @returns {object} All translations for current language
 */
function getAllTranslations () {
  return languages[currentLanguage] || languages[DEFAULT_LANGUAGE]
}

/**
 * Check if language is available
 * @param {string} lang Language code
 * @returns {boolean} True if language is available
 */
function isLanguageAvailable (lang) {
  return lang in languages
}

/**
 * Get available languages
 * @returns {string[]} Array of available language codes
 */
function getAvailableLanguages () {
  return Object.keys(languages)
}

// Initialize with default language
setLanguage(DEFAULT_LANGUAGE)

module.exports = {
  getCurrentLanguage,
  setLanguage,
  t,
  getAllTranslations,
  isLanguageAvailable,
  getAvailableLanguages
}
