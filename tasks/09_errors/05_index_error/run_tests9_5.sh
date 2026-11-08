#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3 1\n10 20 30' $'Value: 20\n'
run_case $'3 5\n10 20 30' $'Error: index out of range\n'
run_case $'3 -1\n10 20 30' $'Value: 30\n'
run_case $'3 -4\n10 20 30' $'Error: index out of range\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
