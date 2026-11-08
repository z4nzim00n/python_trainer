#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f output.txt text.txt' EXIT
run_case $'output.txt\nhello' $'Written: output.txt\n'
check_file "output.txt" "hello"
run_case $'text.txt\nhello world' $'Written: text.txt\n'
check_file "text.txt" "hello world"

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
