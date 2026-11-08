#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\nAda' $'Ada: 3\n'
run_case $'42\nBob' $'Bob: 42\n'
run_case $'0\nX' $'X: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
