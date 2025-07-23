#!/bin/bash

input_dir="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files"
output_dir="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files_format"

mkdir -p "$output_dir"

for fasta in "$input_dir"/*.fasta; do
  file=$(basename "$fasta")
  {
    read header
    echo "$header"
    grep -v '^>' "$fasta" | tr -d '\n' | tr -d '\r' | tr 'a-z' 'A-Z'
    echo
  } < "$fasta" > "$output_dir/$file"
done