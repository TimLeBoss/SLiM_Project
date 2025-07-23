#!/bin/bash

# Dossier contenant les fichiers BCF
folder="/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/BCF_Files/"  # ← à adapter
output_file="/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/Yellow/Nind.txt"

# Vide le fichier de sortie s’il existe
> "$output_file"

# Boucle sur chaque BCF
for bcf in "$folder"/*.bcf; do
    if [ -f "$bcf" ]; then
        filename=$(basename "$bcf")
        # Compter le nombre d’individus avec bcftools
        n=$(bcftools query -l "$bcf" | wc -l)
        echo -e "$filename\t$n" >> "$output_file"
    fi
done