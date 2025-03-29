#!/usr/bin/env bash

SCRIPT_DIR=$(dirname $0)

source $SCRIPT_DIR/.venv/bin/activate

set -x
set -eu
set -o pipefail

isort .
ruff format .
ruff check . --fix
mypy .
pytest
