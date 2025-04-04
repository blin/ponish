#!/usr/bin/env bash

set -x

input_boxes="$1"

while IFS="," read -r infile outfile x y width height; do
  convert "$infile" -set option:random-seed 1234 -crop "${width}x${height}+${x}+${y}" +repage -strip -define png:exclude-chunk=all -define png:compression-level=9 "$outfile";
done < <(tail -n+2 "$input_boxes" )
