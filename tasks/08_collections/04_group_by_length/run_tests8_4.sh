#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "cat dog hello" $'3: cat dog\n5: hello\n'
run_case "a bb ccc" $'1: a\n2: bb\n3: ccc\n'
run_case "hi hi" $'2: hi hi\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
