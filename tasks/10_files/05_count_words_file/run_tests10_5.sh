#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f text.txt' EXIT
printf 'hello world\npython' > text.txt
run_case "text.txt" $'Words: 3\n'
printf 'one' > text.txt
run_case "text.txt" $'Words: 1\n'
printf '' > text.txt
run_case "text.txt" $'Words: 0\n'
run_case "missing.txt" $'Error: file not found\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
