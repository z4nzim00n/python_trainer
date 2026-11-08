#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3" $'Results: 1 4 9\n'
run_case "5" $'Results: 1 4 9 16 25\n'
run_case "1" $'Results: 1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
