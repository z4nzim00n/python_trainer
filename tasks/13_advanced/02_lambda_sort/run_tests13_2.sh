#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\nAda 90\nBob 75\nCy 90' $'Ada: 90\nCy: 90\nBob: 75\n'
run_case $'2\nZoe 100\nAmy 100' $'Amy: 100\nZoe: 100\n'
run_case $'3\nL 5\nM 9\nN 1' $'M: 9\nL: 5\nN: 1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
