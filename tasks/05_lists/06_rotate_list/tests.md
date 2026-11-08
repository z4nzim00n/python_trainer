# PY_05_06. Циклический сдвиг — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests5_6.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `5 0\n1 2 3 4 5` | `1 2 3 4 5\n` |
| `3 5\n1 2 3` | `2 3 1\n` |

## Автотесты

```bash
bash run_tests5_6.sh
```
