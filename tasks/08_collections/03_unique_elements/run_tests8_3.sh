#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'6\n3 1 2 1 3 2' $'Unique: 1 2 3\n'
run_case $'1\n5' $'Unique: 5\n'
run_case $'4\n-1 -1 0 0' $'Unique: -1 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
