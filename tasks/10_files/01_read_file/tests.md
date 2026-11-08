# PY_10_01. Чтение файла — Тесты

## Запуск

```bash
python main.py
```

Эталон:

```bash
python solution.py
python solution_commented.py
```

Скрипт `run_tests10_1.sh` сам находит интерпретатор Python 3.

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `input.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `input.txt` (`abc`, без `\n`) | `abc` |
| `missing.txt` | `Error: file not found\n` |

## Автотесты

```bash
bash run_tests10_1.sh
```
