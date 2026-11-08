# PY_10_03. Копирование файла — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests10_3.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `input.txt\ncopy.txt` | `Copied: input.txt -> copy.txt\n`, файл `copy.txt` совпадает |
| `text.txt\nbackup.txt` | `Copied: text.txt -> backup.txt\n`, файл совпадает |
| `missing.txt\ncopy.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_3.sh
```
