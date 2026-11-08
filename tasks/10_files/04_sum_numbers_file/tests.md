# PY_10_04. Сумма чисел из файла — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests10_4.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `numbers.txt` (`1 2 3\n4 5`) | `Sum: 15\n` |
| `numbers.txt` (`10`) | `Sum: 10\n` |
| `numbers.txt` (пустой) | `Sum: 0\n` |
| `missing.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_4.sh
```
