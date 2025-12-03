import { app, Menu } from 'electron'
import * as actions from '../actions/file'
import i18n from '../../i18n'

const t = i18n.t
const dockMenu = Menu.buildFromTemplate([{
  label: t('menu.dock.open'),
  click (menuItem, browserWindow) {
    if (browserWindow) {
      actions.openFile(browserWindow)
    } else {
      actions.newEditorWindow()
    }
  }
}, {
  label: t('menu.dock.clearRecent'),
  click () {
    app.clearRecentDocuments()
  }
}])

export default dockMenu
