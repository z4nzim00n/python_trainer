#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "level" $'Palindrome: True\n'
run_case "Hello" $'Palindrome: False\n'
run_case "A man a plan a canal Panama" $'Palindrome: True\n'
run_case "" $'Palindrome: True\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
