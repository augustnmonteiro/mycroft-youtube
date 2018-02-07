#!/usr/bin/env bash

found_exe() {
    hash "$1" 2>/dev/null
}
# polkit uses pkcon instead of apt-get
# pkcon runs apt-get in the background
if found_exe pkcon; then
    pkcon install mplayer -y
fi
