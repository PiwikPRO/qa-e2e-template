#!/usr/bin/env bash

# Wait for selenium. It's java application and it takes some time to run it
SELENIUM='http://selenium:4444'
for i in $(seq 1 60); do
  wget -q -O- "$SELENIUM" > /dev/null
  if (( $? != 0 )); then
    echo "[WARNING] Still waiting for selenium on $SELENIUM"
    sleep 1s
  else
    echo "[OK] Selenium on $SELENIUM is up"
    break
  fi
done

set -e

[[ -n "$@" ]] && echo "Limiting tests to $@"

cd ${code_dir}
export PYTHONPATH="$(pwd):PYTHONPATH"
# Comment out framework you won't use in your tests
behave $@
pytest -p no:cacheprovider $@
