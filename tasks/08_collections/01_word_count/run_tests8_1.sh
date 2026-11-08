#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "apple banana apple" $'apple: 2\nbanana: 1\n'
run_case "b a b a c" $'a: 2\nb: 2\nc: 1\n'
run_case "one" $'one: 1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
