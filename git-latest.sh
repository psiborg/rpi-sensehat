#!/usr/bin/env bash

# Prompt user for confirmation
read -p "Warning: This script will discard all local commits and changes. Proceed? (y/n): " confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Operation aborted."
    exit 1
fi

# Discard local changes in tracked files
git reset --hard

# Remove untracked files and directories (if you have any)
git clean -fd

# Fetch the latest changes from origin
git fetch origin

# Reset your branch to the latest commit on the remote
git reset --hard origin/main

# Set executable permissions for all .py and .sh files
chmod 755 *.py *.sh
