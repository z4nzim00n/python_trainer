#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "123" $'Reversed: 321\n'
run_case "1200" $'Reversed: 21\n'
run_case "-45" $'Reversed: -54\n'
run_case "0" $'Reversed: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
