#!/usr/bin/env bash

echo 'Package ...'
mv secrets.py /tmp/
rm -rf ./build/
rm -rf ./dist/
rm -rf ./twitter_makeup.egg-info/
python3.6 setup.py sdist bdist_wheel
echo 'Done 📦'️
