const path = require('path')
const fs = require('fs')

function load (p) {
  const full = path.resolve(p)
  if (!fs.existsSync(full)) return null
  return require(full)
}

function flatten (obj, prefix = '') {
  const res = {}
  for (const k of Object.keys(obj)) {
    const v = obj[k]
    const key = prefix ? `${prefix}.${k}` : k
    if (v && typeof v === 'object') {
      Object.assign(res, flatten(v, key))
    } else {
      res[key] = v
    }
  }
  return res
}

function compare (base, other) {
  const baseFlat = flatten(base)
  const otherFlat = flatten(other)
  const missing = []
  const extra = []
  const untranslated = []

  // Load white list from config file if available
  let whiteList = []
  try {
    const cfgPath = path.resolve(__dirname, 'i18n-config.json')
    if (fs.existsSync(cfgPath)) {
      const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'))
      whiteList = cfg.whiteList || []
    }
  } catch (e) {
    // ignore and use empty whitelist
  }

  for (const k of Object.keys(baseFlat)) {
    if (!(k in otherFlat)) missing.push(k)
    else if (!otherFlat[k] || otherFlat[k] === '') missing.push(k)
    else if (typeof baseFlat[k] === 'string' && baseFlat[k] === otherFlat[k]) {
      // same string as base language -> probably untranslated,
      // but skip keys that are on the whitelist (match by suffix)
      const shouldIgnore = whiteList.some(w => k.endsWith(w))
      if (!shouldIgnore) untranslated.push(k)
    }
  }

  for (const k of Object.keys(otherFlat)) {
    if (!(k in baseFlat)) extra.push(k)
  }

  return { missing, extra, untranslated }
}

function run () {
  const proj = path.resolve(__dirname, '..')
  const rendererEn = load(path.join(proj, 'src', 'renderer', 'i18n', 'en.js'))
  const rendererTr = load(path.join(proj, 'src', 'renderer', 'i18n', 'tr.js'))
  const mainEn = load(path.join(proj, 'src', 'main', 'i18n', 'en.js'))
  const mainTr = load(path.join(proj, 'src', 'main', 'i18n', 'tr.js'))

  if (!rendererEn || !rendererTr || !mainEn || !mainTr) {
    console.error('Could not load one or more i18n files')
    process.exit(1)
  }

  console.log('Comparing renderer i18n...')
  const r = compare(rendererEn, rendererTr)
  console.log('Renderer missing:', r.missing.length)
  console.log('Renderer extra:', r.extra.length)
  console.log('Renderer untranslated (same as en):', r.untranslated ? r.untranslated.length : 0)
  if (r.missing.length) console.log('Missing keys (renderer):\n', r.missing.join('\n'))
  if (r.extra.length) console.log('Extra keys (renderer):\n', r.extra.join('\n'))
  if (r.untranslated && r.untranslated.length) console.log('Untranslated keys (renderer):\n', r.untranslated.join('\n'))

  console.log('\nComparing main i18n...')
  const m = compare(mainEn, mainTr)
  console.log('Main missing:', m.missing.length)
  console.log('Main extra:', m.extra.length)
  console.log('Main untranslated (same as en):', m.untranslated ? m.untranslated.length : 0)
  if (m.missing.length) console.log('Missing keys (main):\n', m.missing.join('\n'))
  if (m.extra.length) console.log('Extra keys (main):\n', m.extra.join('\n'))
  if (m.untranslated && m.untranslated.length) console.log('Untranslated keys (main):\n', m.untranslated.join('\n'))
}

run()
