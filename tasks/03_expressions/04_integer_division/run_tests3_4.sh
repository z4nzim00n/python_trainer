#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "7 3" $'Div: 2\nRem: 1\n'
run_case "10 2" $'Div: 5\nRem: 0\n'
run_case "-7 3" $'Div: -3\nRem: 2\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
