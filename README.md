# LogWatch - Просмотр системных логов через Telegram бота
Утилита для чтения journalctl логов без прав root.

Археректура
```
[ journald ] → (тут логи пишутся) → [ LOGWATCH ] → (фильтрация) → [ всплывающие окна ]
                                         ↓
                                   [ локальный лог-файл ]
                                (на всякий пожарный)
```

## Установка и сборка

### Требования
- Python 3.14+
- Poetry

### Установка зависимостей
```bash
poetry install --no-root
pip install pyinstaller
```
### Сборка/разборка
```bash
# Сборка ультилиты полностью
make build
make rebuild

# Индивидуальная сборка
make journal_reader

# Тесты Сэр
make test

# Почистить все
make clean
```

### Запуск
```bash
./journal_reader
```
