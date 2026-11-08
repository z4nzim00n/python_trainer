#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5 2\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'5 0\n1 2 3 4 5' $'1 2 3 4 5\n'
run_case $'3 5\n1 2 3' $'2 3 1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
