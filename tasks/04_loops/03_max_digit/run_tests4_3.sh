#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "123" $'Max digit: 3\n'
run_case "9005" $'Max digit: 9\n'
run_case "-47" $'Max digit: 7\n'
run_case "0" $'Max digit: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
