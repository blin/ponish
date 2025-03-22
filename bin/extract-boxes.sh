#!/usr/bin/env bash

set -x

input_image="$1"
input_boxes="$2"

while IFS="," read -r outfile x y width height; do
  convert "$input_image" -crop "${width}x${height}+${x}+${y}" "$outfile";
done < <(tail -n+2 "$input_boxes" )
