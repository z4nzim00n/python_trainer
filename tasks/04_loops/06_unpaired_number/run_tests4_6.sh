#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 2 1' $'Unpaired: 3\n'
run_case $'7\n4 4 9 9 5 5 7' $'Unpaired: 7\n'
run_case $'1\n42' $'Unpaired: 42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
