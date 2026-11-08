#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'4\n1 2 3 4' $'4 3 2 1\n'
run_case $'1\n10' $'10\n'
run_case $'3\n-1 0 5' $'5 0 -1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
