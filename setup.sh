#!/usr/bin/env sh

echo "--- Installation of Pillow for MacOS ---\n Guide: https://pillow.readthedocs.io/en/latest/installation.html#building-from-source \n"

echo "Installing Xcode command line tools \n"
xcode-select --install

echo "-- Homebrew needed: install it from https://brew.sh/ --\n"

echo "Installing 'libjpeg libtiff little-cms2 openjpeg webp' dependencies from brew \n"
brew install libjpeg libtiff little-cms2 openjpeg webp

echo "Installing 'libraqm' -freetype harfbuzz fribidi- dependencies for MacOS \n"
brew install freetype harfbuzz fribidi

echo "-- Installing Pillow --"
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow --no-binary :all:
