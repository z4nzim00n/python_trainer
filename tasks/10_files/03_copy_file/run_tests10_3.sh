#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f input.txt copy.txt text.txt backup.txt' EXIT
printf 'hello\nworld\n' > input.txt
run_case $'input.txt\ncopy.txt' $'Copied: input.txt -> copy.txt\n'
check_file "copy.txt" $'hello\nworld\n'
printf 'abc' > text.txt
run_case $'text.txt\nbackup.txt' $'Copied: text.txt -> backup.txt\n'
check_file "backup.txt" "abc"
run_case $'missing.txt\ncopy.txt' $'Error: file not found\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
