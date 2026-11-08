# PY_09_05. Индекс вне диапазона — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests9_5.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `3 1\n10 20 30` | `Value: 20\n` |
| `3 5\n10 20 30` | `Error: index out of range\n` |
| `3 -1\n10 20 30` | `Value: 30\n` |
| `3 -4\n10 20 30` | `Error: index out of range\n` |

## Автотесты

```bash
bash run_tests9_5.sh
```
