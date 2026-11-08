#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\nHello, World!' $'Khoor, Zruog!\n'
run_case $'1\nabc XYZ' $'bcd YZA\n'
run_case $'0\nTest' $'Test\n'
run_case $'26\nTest' $'Test\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
