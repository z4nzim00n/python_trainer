#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2 3" $'A: 4\nB: 9\n'
run_case "-4 5" $'A: 16\nB: 25\n'
run_case "0 0" $'A: 0\nB: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
