#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "4" $'Positive: True\nEven: True\n'
run_case "-3" $'Positive: False\nEven: False\n'
run_case "0" $'Positive: False\nEven: True\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
