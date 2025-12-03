import { t } from '@/i18n'

// Helper function to get translated options
function getTitleBarStyleOptions () {
  return [{
    label: t('preferences.general.window.titleBarStyle.options.custom'),
    value: 'custom'
  }, {
    label: t('preferences.general.window.titleBarStyle.options.native'),
    value: 'native'
  }]
}

// Zoom options don't need translation (they're percentages)
export const zoomOptions = [{
  label: '50.0%',
  value: 0.5
}, {
  label: '62.5%',
  value: 0.625
}, {
  label: '75.0%',
  value: 0.75
}, {
  label: '87.5%',
  value: 0.875
}, {
  label: '100.0%',
  value: 1.0
}, {
  label: '112.5%',
  value: 1.125
}, {
  label: '125.0%',
  value: 1.25
}, {
  label: '137.5%',
  value: 1.375
}, {
  label: '150.0%',
  value: 1.5
}, {
  label: '162.5%',
  value: 1.625
}, {
  label: '175.0%',
  value: 1.75
}, {
  label: '187.5%',
  value: 1.875
}, {
  label: '200.0%',
  value: 2.0
}]

function getFileSortByOptions () {
  return [{
    label: t('preferences.general.sidebar.fileSortBy.options.created'),
    value: 'created'
  }, {
    label: t('preferences.general.sidebar.fileSortBy.options.modified'),
    value: 'modified'
  }, {
    label: t('preferences.general.sidebar.fileSortBy.options.title'),
    value: 'title'
  }]
}

function getLanguageOptions () {
  return [{
    label: t('preferences.general.misc.userInterfaceLanguage.options.en'),
    value: 'en'
  }, {
    label: t('preferences.general.misc.userInterfaceLanguage.options.tr'),
    value: 'tr'
  }]
}

// Export functions that return translated options
export const titleBarStyleOptions = getTitleBarStyleOptions()
export const fileSortByOptions = getFileSortByOptions()
export const languageOptions = getLanguageOptions()

// Export getter functions for reactive updates
export function getTitleBarStyleOptionsFn () {
  return getTitleBarStyleOptions()
}

export function getFileSortByOptionsFn () {
  return getFileSortByOptions()
}

export function getLanguageOptionsFn () {
  return getLanguageOptions()
}
