#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "abc123" $'Letters: 3\nDigits: 3\n'
run_case "Hello, World!" $'Letters: 10\nDigits: 0\n'
run_case "a1b2c3" $'Letters: 3\nDigits: 3\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
