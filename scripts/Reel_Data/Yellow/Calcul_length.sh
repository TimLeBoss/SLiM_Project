#!/bin/bash

input_dir="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files"
output_file="/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/Yellow/length.txt"

> "$output_file"

for fasta in "$input_dir"/*.fasta; do
  filename=$(basename "$fasta")
  length=$(grep -v '^>' "$fasta" | tr -d '\n' | wc -m)
  echo -e "${filename}\t${length}"
done | sort -V > "$output_file"

echo "Longueurs écrites et triées dans $output_file"
