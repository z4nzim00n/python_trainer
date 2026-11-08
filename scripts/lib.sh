#!/usr/bin/env bash
# scripts/lib.sh — общие функции для run_tests.sh в заданиях Python-тренажёра.
#
# Источник решения задаётся переменной SOURCE_FILE (по умолчанию main.py):
#   SOURCE_FILE=solution.py bash run_tests1_1.sh
#
# Ожидаемый вывод в run_case — точные байты. Для переносов строк используй
# ANSI-C кавычки: run_case "2 2" $'4\n'. Вывод программы нормализуется:
# \r\n -> \n.

_LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$_LIB_DIR/.." && pwd)"

SOURCE_FILE="${SOURCE_FILE:-main.py}"

# Ищем интерпретатор: переменная PYTHON, затем python, py, python3.
# На Windows команда python3 может быть заглушкой Microsoft Store, поэтому
# она идёт последней.
PYTHON_BIN="${PYTHON:-}"
if [ -z "$PYTHON_BIN" ]; then
  for _candidate in python py python3; do
    if command -v "$_candidate" >/dev/null 2>&1; then
      PYTHON_BIN="$(command -v "$_candidate")"
      break
    fi
  done
  unset _candidate
fi

export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

compile() {
  if [ -z "$PYTHON_BIN" ]; then
    echo "Интерпретатор Python 3 не найден." >&2
    echo "Установите Python 3 либо задайте PYTHON полным путём." >&2
    return 1
  fi

  # Проверка синтаксиса без создания __pycache__.
  "$PYTHON_BIN" -c 'import sys; p = sys.argv[1]; compile(open(p, encoding="utf-8").read(), p, "exec")' "$SOURCE_FILE"
}

run_program() {
  "$PYTHON_BIN" "$SOURCE_FILE" "$@"
}

_compare_and_report() {
  local label="$1" expected="$2"
  printf '%s' "$expected" > /tmp/expected.out
  if cmp -s /tmp/actual.out /tmp/expected.out; then
    echo "OK:   $label -> '$expected'"
  else
    echo "FAIL: $label -> получили '$(cat -A /tmp/actual.out)', ждали '$(cat -A /tmp/expected.out)'"
    FAILED=1
  fi
}

# run_case "вход" "ожидаемый_вывод" — вход через printf (добавляет \n)
run_case() {
  local input="$1" expected="$2"
  printf '%s\n' "$input" | run_program | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input'" "$expected"
}

# run_case_noeol "вход" "ожидаемый_вывод" — вход БЕЗ завершающего \n
run_case_noeol() {
  local input="$1" expected="$2"
  printf '%s' "$input" | run_program | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input' (без \\n)" "$expected"
}

# run_case_devnull "ожидаемый_вывод" — вход полностью пуст (EOF до первого символа)
run_case_devnull() {
  local expected="$1"
  run_program < /dev/null | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "(/dev/null)" "$expected"
}

# run_case_args "аргументы" "вход" "ожидаемый_вывод"
run_case_args() {
  local args="$1" input="$2" expected="$3"
  printf '%s\n' "$input" | run_program $args | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "args='$args' input='$input'" "$expected"
}

# check_file "путь" "ожидаемое_содержимое" — проверяет файл, созданный программой.
check_file() {
  local file="$1" expected="$2"
  printf '%s' "$expected" > /tmp/expected_file.out
  if [ ! -f "$file" ]; then
    echo "FAIL: файл '$file' не создан"
    FAILED=1
    return
  fi
  tr -d '\r' < "$file" > /tmp/actual_file.out || true
  if cmp -s /tmp/actual_file.out /tmp/expected_file.out; then
    echo "OK:   файл '$file' -> '$expected'"
  else
    echo "FAIL: файл '$file' -> получили '$(cat -A /tmp/actual_file.out)', ждали '$(cat -A /tmp/expected_file.out)'"
    FAILED=1
  fi
}
