#!/bin/bash
set -euo pipefail


http --print=hb "$@" | (
    while read line; do
        echo "${line}"
    done
    html2text <&0
)
