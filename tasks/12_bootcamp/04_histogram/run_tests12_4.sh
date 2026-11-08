#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'6\n1 2 2 3 3 3' $'1: *\n2: **\n3: ***\n'
run_case $'3\n5 5 5' $'5: ***\n'
run_case $'4\n3 1 3 1' $'1: **\n3: **\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
