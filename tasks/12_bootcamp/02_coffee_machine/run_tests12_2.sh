#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'50\n10 10 10 10 10 0' $'Change: 0\n'
run_case $'75\n25 25 0' $'Need: 25\n'
run_case $'30\n5 10 20 0' $'Change: 5\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
