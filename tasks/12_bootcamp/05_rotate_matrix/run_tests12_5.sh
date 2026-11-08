#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'2\n1 2\n3 4' $'3 1\n4 2\n'
run_case $'3\n1 2 3\n4 5 6\n7 8 9' $'7 4 1\n8 5 2\n9 6 3\n'
run_case $'1\n42' $'42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
