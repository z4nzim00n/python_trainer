#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'2\n1 2\n3 4\n5 6\n7 8' $'6 8\n10 12\n'
run_case $'1\n5\n6' $'11\n'
run_case $'2\n1 -1\n0 2\n-1 1\n0 -2' $'0 0\n0 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
