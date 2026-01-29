

# Настройка горячих клавиш в VS Code
Ctrl + Shift + O - **открывает список всех функций/методов (Go to Symbol in File).**
Ctrl + Shift + ] / Ctrl + Shift + [ - **сворачивание/разворачивание функции/блока кода.**



## Как настроить свои горячие клавиши
Нажми **Ctrl+Shift+P**
  → введи **Preferences: Open Keyboard Shortcuts (JSON)**
    → откроется keybindings.json.

    
## Добавь туда нужные сочетания. Например:
[
  {
    // (прыжок к парной скобке)
    "key": "ctrl+space",
    "command": "editor.action.jumpToBracket", # (прыжок к парной скобке)
    "when": "editorTextFocus"
  },
  {
    // (выделить всё содержимое скобок вместе со скобками)
    "key": "ctrl+down",
    "command": "editor.action.selectToBracket"
  },
  {
    // список всех функций/методов в файле
    "key": "ctrl+up",
    "command": "workbench.action.gotoSymbol"
  },
  {
    // прыжок на последнюю точку редактирования.
    "key": "ctrl+shift+backspace",
    "command": "workbench.action.navigateToLastEditLocation",
    "when": "editorTextFocus"
  },
  {
    // Сдвиг курсора на 1 символ в правую сторону
    "key": "shift+space",
    "command": "cursorRight",
    "when": "editorTextFocus"
  }
]



<!-- НЕ РАБОТАЕТ
Нажми Ctrl+Shift+P → введи Preferences: Open Keyboard Shortcuts (JSON) → откроется keybindings.json.
Добавь туда нужные сочетания. Например:
[
    {
        "key": "ctrl+alt+down",      // переход к следующей функции
        "command": "editor.action.goToNextSymbolFromResult"
    },
    {
        "key": "ctrl+alt+up",        // переход к предыдущей функции
        "command": "editor.action.goToPreviousSymbolFromResult"
    }
] -->


## Не проверины.
Что это даёт?

```bash
Скобки
Ctrl+M → прыгнуть к парной скобке
Ctrl+Shift+M → выделить содержимое внутри

Строки
Alt+↑/↓ → перенести строку вверх/вниз
Shift+Alt+↑/↓ → скопировать строку вверх/вниз
Ctrl+D → удалить строку
Ctrl+L → выделить строку целиком

Функции (через расширение)
Ctrl+Alt+↓ → к следующей функции
Ctrl+Alt+↑ → к предыдущей функции

Символы / переходы
Ctrl+Shift+O → список всех функций/методов в файле
Ctrl+Alt+←/→ → навигация назад/вперёд по истории курсора
[
  // --- Скобки ---
  {
    "key": "ctrl+m",
    "command": "editor.action.jumpToBracket",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+shift+m",
    "command": "editor.action.selectToBracket",
    "when": "editorTextFocus"
  },

  // --- Строки ---
  {
    "key": "alt+up",
    "command": "editor.action.moveLinesUpAction",
    "when": "editorTextFocus"
  },
  {
    "key": "alt+down",
    "command": "editor.action.moveLinesDownAction",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+alt+up",
    "command": "editor.action.copyLinesUpAction",
    "when": "editorTextFocus"
  },
  {
    "key": "shift+alt+down",
    "command": "editor.action.copyLinesDownAction",
    "when": "editorTextFocus"
  },

  // --- Удаление и выделение ---
  {
    "key": "ctrl+d",
    "command": "editor.action.deleteLines",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+l",
    "command": "expandLineSelection",
    "when": "editorTextFocus"
  },

  // --- Функции (через расширение "Go to Next/Previous Member") ---
  {
    "key": "ctrl+alt+down",
    "command": "gotoNextPreviousMember.nextMember",
    "when": "editorTextFocus"
  },
  {
    "key": "ctrl+alt+up",
    "command": "gotoNextPreviousMember.previousMember",
    "when": "editorTextFocus"
  },

  // --- Символы / методы / классы ---
  {
    "key": "ctrl+shift+o",
    "command": "workbench.action.gotoSymbol"
  },
  {
    "key": "ctrl+alt+left",
    "command": "workbench.action.navigateBack"
  },
  {
    "key": "ctrl+alt+right",
    "command": "workbench.action.navigateForward"
  }
]
