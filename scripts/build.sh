#!/bin/bash
set -e

echo "Cleaning build/dist folders..."
sudo rm -rf build dist graphutil.egg-info

echo "Running build..."
pip install build
python -m build

echo "Done."