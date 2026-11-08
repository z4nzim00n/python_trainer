#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f input.txt missing.txt' EXIT
printf 'hello\nworld\n' > input.txt
run_case "input.txt" $'hello\nworld\n'
printf 'abc' > input.txt
run_case "input.txt" "abc"
run_case "missing.txt" $'Error: file not found\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
