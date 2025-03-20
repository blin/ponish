#!/usr/bin/env bash

SCRIPT_DIR=$(dirname $0)

source $SCRIPT_DIR/.venv/bin/activate

ruff format .
ruff check . --fix
mypy .
