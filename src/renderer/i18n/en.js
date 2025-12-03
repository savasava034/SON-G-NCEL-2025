/**
 * English (en) language file
 * This file contains all English translations for MarkText
 */

export default {
  // Menu translations
  menu: {
    // File menu
    file: {
      label: '&File',
      newTab: 'New Tab',
      newWindow: 'New Window',
      openFile: 'Open File...',
      openFolder: 'Open Folder...',
      openRecent: 'Open Recent',
      clearRecentlyUsed: 'Clear Recently Used',
      save: 'Save',
      saveAs: 'Save As...',
      autoSave: 'Auto Save',
      moveTo: 'Move To...',
      rename: 'Rename...',
      import: 'Import...',
      export: 'Export',
      exportHtml: 'HTML',
      exportPdf: 'PDF',
      print: 'Print',
      preferences: 'Preferences...',
      closeTab: 'Close Tab',
      closeWindow: 'Close Window',
      quit: 'Quit'
    },
    // Edit menu
    edit: {
      label: '&Edit',
      undo: 'Undo',
      redo: 'Redo',
      cut: 'Cut',
      copy: 'Copy',
      paste: 'Paste',
      copyAsMarkdown: 'Copy as Markdown',
      copyAsHtml: 'Copy as HTML',
      pasteAsPlainText: 'Paste as Plain Text',
      selectAll: 'Select All',
      duplicate: 'Duplicate',
      createParagraph: 'Create Paragraph',
      deleteParagraph: 'Delete Paragraph',
      find: 'Find',
      findNext: 'Find Next',
      findPrevious: 'Find Previous',
      replace: 'Replace',
      findInFolder: 'Find in Folder',
      screenshot: 'Screenshot',
      lineEnding: 'Line Ending',
      lineEndingCrlf: 'Carriage return and line feed (CRLF)',
      lineEndingLf: 'Line feed (LF)'
    },
    // Paragraph menu
    paragraph: {
      label: '&Paragraph',
      heading1: 'Heading 1',
      heading2: 'Heading 2',
      heading3: 'Heading 3',
      heading4: 'Heading 4',
      heading5: 'Heading 5',
      heading6: 'Heading 6',
      promoteHeading: 'Promote Heading',
      demoteHeading: 'Demote Heading',
      table: 'Table',
      codeFences: 'Code Fences',
      quoteBlock: 'Quote Block',
      mathBlock: 'Math Block',
      htmlBlock: 'Html Block',
      orderedList: 'Ordered List',
      bulletList: 'Bullet List',
      taskList: 'Task List',
      looseListItem: 'Loose List Item',
      paragraph: 'Paragraph',
      horizontalRule: 'Horizontal Rule',
      frontMatter: 'Front Matter'
    },
    // Format menu
    format: {
      label: 'F&ormat',
      bold: 'Bold',
      italic: 'Italic',
      underline: 'Underline',
      superscript: 'Superscript',
      subscript: 'Subscript',
      highlight: 'Highlight',
      inlineCode: 'Inline Code',
      inlineMath: 'Inline Math',
      strikethrough: 'Strikethrough',
      hyperlink: 'Hyperlink',
      image: 'Image',
      clearFormatting: 'Clear Formatting'
    },
    // View menu
    view: {
      label: '&View',
      commandPalette: 'Command Palette...',
      sourceCodeMode: 'Source Code Mode',
      typewriterMode: 'Typewriter Mode',
      focusMode: 'Focus Mode',
      showSidebar: 'Show Sidebar',
      showTabBar: 'Show Tab Bar',
      toggleTableOfContents: 'Toggle Table of Contents',
      reloadImages: 'Reload Images',
      showDeveloperTools: 'Show Developer Tools',
      reloadWindow: 'Reload window'
    },
    // Window menu
    window: {
      label: '&Window',
      minimize: 'Minimize',
      alwaysOnTop: 'Always on Top',
      zoomIn: 'Zoom In',
      zoomOut: 'Zoom Out',
      showInFullScreen: 'Show in Full Screen',
      bringAllToFront: 'Bring All to Front'
    },
    // Theme menu
    theme: {
      label: '&Theme',
      cadmiumLight: 'Cadmium Light',
      dark: 'Dark',
      graphiteLight: 'Graphite Light',
      materialDark: 'Material Dark',
      oneDark: 'One Dark',
      ulyssesLight: 'Ulysses Light'
    },
    // Help menu
    help: {
      label: '&Help',
      quickStart: 'Quick Start...',
      markdownReference: 'Markdown Reference...',
      changelog: 'Changelog...',
      donateViaOpenCollective: 'Donate via Open Collective...',
      feedbackViaTwitter: 'Feedback via Twitter...',
      reportIssue: 'Report Issue or Request Feature...',
      website: 'Website...',
      watchOnGithub: 'Watch on GitHub...',
      followUsOnGithub: 'Follow us on Github...',
      followUsOnTwitter: 'Follow us on Twitter...',
      license: 'License...',
      checkForUpdates: 'Check for updates...',
      aboutMarkText: 'About MarkText...'
    },
    // MarkText menu (macOS only)
    marktext: {
      label: 'MarkText',
      aboutMarkText: 'About MarkText',
      checkForUpdates: 'Check for updates...',
      preferences: 'Preferences',
      services: 'Services',
      hideMarkText: 'Hide MarkText',
      hideOthers: 'Hide Others',
      showAll: 'Show All',
      quitMarkText: 'Quit MarkText'
    },
    // Dock menu (macOS only)
    dock: {
      open: 'Open...',
      clearRecent: 'Clear Recent'
    },
    // Preferences Edit menu
    prefEdit: {
      label: 'Edit',
      cut: 'Cut',
      copy: 'Copy',
      paste: 'Paste',
      selectAll: 'Select All'
    }
  },

  // Preferences translations
  preferences: {
    title: 'Preferences',
    // Categories
    categories: {
      general: 'General',
      editor: 'Editor',
      markdown: 'Markdown',
      spelling: 'Spelling',
      theme: 'Theme',
      image: 'Image',
      keyBindings: 'Key Bindings'
    },
    // General preferences
    general: {
      title: 'General',
      autoSave: {
        title: 'Auto Save:',
        description: 'Automatically save document changes'
      },
      autoSaveDelay: {
        description: 'Delay following document edit before automatically saving'
      },
      window: {
        title: 'Window:',
        titleBarStyle: {
          description: 'Title bar style',
          notes: 'Requires restart.',
          options: {
            custom: 'Custom',
            native: 'Native'
          }
        },
        hideScrollbar: {
          description: 'Hide scrollbars'
        },
        openFilesInNewWindow: {
          description: 'Open files in new window'
        },
        openFolderInNewWindow: {
          description: 'Open folders in new window'
        },
        zoom: {
          description: 'Zoom'
        }
      },
      sidebar: {
        title: 'Sidebar:',
        wordWrapInToc: {
          description: 'Wrap text in table of contents'
        },
        fileSortBy: {
          description: 'Sort field for files in open folders',
          options: {
            created: 'Creation time',
            modified: 'Modification time',
            title: 'Title'
          }
        }
      },
      startup: {
        title: 'Action on startup:',
        openDefaultDirectory: 'Open the default directory',
        selectFolder: 'Select Folder',
        openBlankPage: 'Open a blank page',
        restoreLastSession: 'Restore last editor session'
      },
      misc: {
        title: 'Misc:',
        userInterfaceLanguage: {
          description: 'User interface language',
          options: {
            en: 'English',
            tr: 'Türkçe'
          }
        }
      }
    }
  },

  // Common translations
  common: {
    searchPreferences: 'Search preferences'
  }
}
