#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'6\n1 2 3 4 5 6' $'Sum: 21\n'
run_case $'1\n10' $'Sum: 10\n'
run_case $'5\n-1 1 -2 2 0' $'Sum: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
