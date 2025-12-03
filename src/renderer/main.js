import Vue from 'vue'
import VueElectron from 'vue-electron'
import sourceMapSupport from 'source-map-support'
import bootstrapRenderer from './bootstrap'
import VueRouter from 'vue-router'
import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'
import axios from './axios'
import store from './store'
import './assets/symbolIcon'
import {
  Dialog,
  Form,
  FormItem,
  InputNumber,
  Button,
  Tooltip,
  Upload,
  Slider,
  Checkbox,
  ColorPicker,
  Col,
  Row,
  Tree,
  Autocomplete,
  Switch,
  Select,
  Option,
  Radio,
  RadioGroup,
  Table,
  TableColumn,
  Tabs,
  TabPane,
  Input
} from 'element-ui'
import services from './services'
import routes from './router'
import { addElementStyle } from '@/util/theme'
import { t, setLanguage } from './i18n'

import './assets/styles/index.css'
import './assets/styles/printService.css'

// -----------------------------------------------

// Decode source map in production - must be registered first
sourceMapSupport.install({
  environment: 'node',
  handleUncaughtExceptions: false,
  hookRequire: false
})

global.marktext = {}
bootstrapRenderer()

addElementStyle()

// -----------------------------------------------
// Be careful when changing code before this line!

// Configure Vue
locale.use(lang)

Vue.use(Dialog)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(InputNumber)
Vue.use(Button)
Vue.use(Tooltip)
Vue.use(Upload)
Vue.use(Slider)
Vue.use(Checkbox)
Vue.use(ColorPicker)
Vue.use(Col)
Vue.use(Row)
Vue.use(Tree)
Vue.use(Autocomplete)
Vue.use(Switch)
Vue.use(Select)
Vue.use(Option)
Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(Input)

Vue.use(VueRouter)

Vue.use(VueElectron)
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

// Add i18n support to Vue
Vue.prototype.$t = t

// Initialize i18n with user's language preference from store and connect
// Element UI locale to our translations. We try to load an Element UI
// language pack that matches the app language; if it's missing we fall
// back to English. Also make Element UI delegate message lookup to our
// i18n.t when supported.
try {
  if (typeof locale.i18n === 'function') {
    // Let Element UI use our translator function for message lookups
    locale.i18n((key, value) => t(key))
  }
} catch (e) {
  // ignore if locale.i18n isn't present
}

store.watch(
  state => state.preferences.language,
  (newLang) => {
    const langToSet = newLang || 'tr'
    setLanguage(langToSet)

    // Try to switch Element UI to matching pack. First prefer local project
    // locale files (src/renderer/element-locales/<lang>.js) then fall back to
    // element-ui package locale files, finally fallback to English.
    const tryUseLocale = (langCode) => {
      // try project-local locale first
      try {
        // eslint-disable-next-line global-require, import/no-dynamic-require
        const projectLocal = require(`./element-locales/${langCode}.js`)
        if (projectLocal) {
          locale.use(projectLocal)
          return true
        }
      } catch (err) {
        // ignore, try package locale next
      }

      try {
        // eslint-disable-next-line global-require, import/no-dynamic-require
        const elLang = require(`element-ui/lib/locale/lang/${langCode}`)
        if (elLang) {
          locale.use(elLang)
          return true
        }
      } catch (err) {
        return false
      }
    }

    if (!tryUseLocale(langToSet)) {
      // try english as last resort
      tryUseLocale('en')
    }
  },
  { immediate: true }
)

services.forEach(s => {
  Vue.prototype['$' + s.name] = s[s.name]
})

const router = new VueRouter({
  routes: routes(global.marktext.env.type)
})

/* eslint-disable no-new */
new Vue({
  store,
  router,
  template: '<router-view class="view"></router-view>'
}).$mount('#app')
