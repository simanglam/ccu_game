#!/bin/sh

source ./venv/bin/activate
python ./backend/main.py & python ./game/main.py
