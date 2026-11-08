# PY_10_06. Статистика файла — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests10_6.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `text.txt` (`hello world\npython\n`) | `Lines: 2\nWords: 3\nChars: 17\n` |
| `text.txt` (`abc`) | `Lines: 1\nWords: 1\nChars: 3\n` |
| `text.txt` (пустой) | `Lines: 0\nWords: 0\nChars: 0\n` |
| `missing.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_6.sh
```
