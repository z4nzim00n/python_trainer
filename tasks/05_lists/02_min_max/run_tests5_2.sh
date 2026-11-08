#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 7 2 9 4' $'Min: 2\nMax: 9\n'
run_case $'3\n-4 -1 -9' $'Min: -9\nMax: -1\n'
run_case $'1\n5' $'Min: 5\nMax: 5\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
