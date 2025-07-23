#!/bin/bash

input="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files/Panubis1.0_genomic_nochr.fa"
output_dir="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files"

mkdir -p "$output_dir"

gawk -v outdir="$output_dir" '
  function toupper_and_replaceN(seq,    i, c, outseq) {
    outseq = ""
    for (i = 1; i <= length(seq); i++) {
      c = substr(seq, i, 1)
      # Convertir en majuscule
      if (c ~ /[a-z]/)
        c = toupper(c)
      # Remplacer les N par A
      if (c == "N")
        c = "A"
      outseq = outseq c
    }
    return outseq
  }

  /^>/ {
    count++
    if (count > 22) exit
    if (out) close(out)
    split($0, header, " ")
    id = substr(header[1], 2)
    out = outdir "/" id ".fasta"
    print $0 >> out
    next
  }

  count <= 22 {
    print toupper_and_replaceN($0) >> out
  }
' "$input"
