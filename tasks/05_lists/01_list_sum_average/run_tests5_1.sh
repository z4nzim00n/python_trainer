#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'4\n1 2 3 4' $'Sum: 10\nAverage: 2.50\n'
run_case $'3\n2 2 2' $'Sum: 6\nAverage: 2.00\n'
run_case $'1\n-5' $'Sum: -5\nAverage: -5.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
