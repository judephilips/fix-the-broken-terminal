#!/bin/bash
set -u

mkdir -p /logs/verifier

# pytest is baked into the environment image (environment/Dockerfile).
if pytest /tests/test_outputs.py -rA --ctrf=/logs/verifier/ctrf.json; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
