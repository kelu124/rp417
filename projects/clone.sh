#!/usr/bin/env bash
# Shallow-clone (or update) every repo listed in repos.txt into projects/<category>/<repo>.
set -u
cd "$(dirname "$0")"
grep -vE '^\s*(#|$)' repos.txt | while read -r cat repo; do
  dest="$cat/${repo#*/}"
  if [ -d "$dest/.git" ]; then
    git -C "$dest" pull --ff-only -q && echo "updated $repo" || echo "FAILED update $repo"
  else
    mkdir -p "$cat"
    git clone -q --depth 1 "https://github.com/$repo.git" "$dest" && echo "cloned  $repo" || echo "FAILED  $repo"
  fi
done
