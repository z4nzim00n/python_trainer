#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2 3" $'Sum: 5\n'
run_case "-4 4" $'Sum: 0\n'
run_case "100 200" $'Sum: 300\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
