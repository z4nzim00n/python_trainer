#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 1 4 1 5' $'1 1 3 4 5\n'
run_case $'3\n-1 5 0' $'-1 0 5\n'
run_case $'4\n9 9 2 2' $'2 2 9 9\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
