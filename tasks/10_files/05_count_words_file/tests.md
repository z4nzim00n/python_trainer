# PY_10_05. Слова в файле — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests10_5.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `text.txt` (`hello world\npython`) | `Words: 3\n` |
| `text.txt` (`one`) | `Words: 1\n` |
| `text.txt` (пустой) | `Words: 0\n` |
| `missing.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_5.sh
```
