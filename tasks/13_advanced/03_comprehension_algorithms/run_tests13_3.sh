#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5' $'Sum: 20\n'
run_case $'4\n2 2 2 2' $'Sum: 16\n'
run_case $'3\n1 3 5' $'Sum: 0\n'
run_case $'4\n-2 1 2 3' $'Sum: 8\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
