#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5' $'Count: 5\nSum: 15\nMin: 1\nMax: 5\nAverage: 3.00\n'
run_case $'1\n7' $'Count: 1\nSum: 7\nMin: 7\nMax: 7\nAverage: 7.00\n'
run_case $'3\n-2 0 2' $'Count: 3\nSum: 0\nMin: -2\nMax: 2\nAverage: 0.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
