#!/usr/bin/env bash

set -x

input_boxes="$1"

while IFS="," read -r infile outfile x y width height; do
  convert "$infile" -crop "${width}x${height}+${x}+${y}" "$outfile";
done < <(tail -n+2 "$input_boxes" )
