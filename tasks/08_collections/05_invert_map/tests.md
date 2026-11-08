# PY_08_05. Инверсия словаря — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests8_5.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3\na 1\nb 2\nc 1` | `1: a c\n2: b\n` |
| `3\nm 10\nn 2\no 10` | `2: n\n10: m o\n` |
| `2\nleft 10\nright 10` | `10: left right\n` |

## Автотесты

```bash
bash run_tests8_5.sh
```
