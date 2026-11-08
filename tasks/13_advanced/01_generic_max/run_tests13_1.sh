#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 7 2 9 4' $'Max: 9\n'
run_case $'1\n-5' $'Max: -5\n'
run_case $'4\n10 10 1 2' $'Max: 10\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
