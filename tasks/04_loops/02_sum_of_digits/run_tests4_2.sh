#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "123" $'Sum: 6\n'
run_case "9005" $'Sum: 14\n'
run_case "-47" $'Sum: 11\n'
run_case "0" $'Sum: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
