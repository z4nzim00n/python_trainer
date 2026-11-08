#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Hello" $'Upper: HELLO\nLower: hello\n'
run_case "PyThOn" $'Upper: PYTHON\nLower: python\n'
run_case "123" $'Upper: 123\nLower: 123\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
