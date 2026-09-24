#!/usr/bin/env bash

STUDENTS_FILE="students.txt"

if [ ! -f "$STUDENTS_FILE" ]; then
  echo "$STUDENTS_FILE is missing!"
  exit 1
fi

while read -r student url || [ -n "$student" ]; do
  [[ -z "$student" || "$student" =~ ^# ]] && continue

  if [ -d "$student" ]; then
    echo "=== Updating: $student ==="
    git -C "$student" pull --ff-only
  else
    echo "=== Cloning: $student ==="
    git clone "$url" "$student"
  fi
  echo ""
done <"$STUDENTS_FILE"

echo "Done!"
