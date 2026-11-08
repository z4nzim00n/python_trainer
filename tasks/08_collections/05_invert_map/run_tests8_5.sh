#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\na 1\nb 2\nc 1' $'1: a c\n2: b\n'
run_case $'3\nm 10\nn 2\no 10' $'2: n\n10: m o\n'
run_case $'2\nleft 10\nright 10' $'10: left right\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
