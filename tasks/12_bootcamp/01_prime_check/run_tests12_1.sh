#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "17" $'Prime: True\n'
run_case "2" $'Prime: True\n'
run_case "1" $'Prime: False\n'
run_case "9" $'Prime: False\n'
run_case "-7" $'Prime: False\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
