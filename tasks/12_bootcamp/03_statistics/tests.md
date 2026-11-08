# PY_12_03. Статистика — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests12_3.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5\n1 2 3 4 5` | `Count: 5\nSum: 15\nMin: 1\nMax: 5\nAverage: 3.00\n` |
| `1\n7` | `Count: 1\nSum: 7\nMin: 7\nMax: 7\nAverage: 7.00\n` |
| `3\n-2 0 2` | `Count: 3\nSum: 0\nMin: -2\nMax: 2\nAverage: 0.00\n` |

## Автотесты

```bash
bash run_tests12_3.sh
```
