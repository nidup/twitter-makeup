#!/usr/bin/env bash

echo 'Publish ...'

python3.6 -m twine upload dist/*

mv /tmp/secrets.py ./

echo 'Done 🚀'
