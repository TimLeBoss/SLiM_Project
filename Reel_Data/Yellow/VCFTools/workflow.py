from gwf import Workflow
import itertools

gwf = Workflow()
Folder_BCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/BCF_Files/"
Folder_VCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/VCF_Files/"
Folder_Pi = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Amboseli_Yellow/Pi_Values/"
Chr = [i for i in range (1,22)]
#Chr = [1]

for i in Chr:
    gwf.target(
        name=f'Reel_VCF_{i}',
        inputs=[],
        outputs=[Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << "vcftools --bcf "+Folder_BCF+f"ref.shapeit_all.{i}.yellow.bcf --recode --out "+Folder_VCF+f"ref.shapeit_all.{i}.yellow" 
    

    gwf.target(
        name=f'Reel_Pi_{i}',
        inputs=[Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        outputs=[Folder_Pi+f"ref.shapeit_all.{i}.yellow.windowed.pi"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << "vcftools --vcf "+Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf --max-missing 1 --window-pi 10000000000 --out "+Folder_Pi+f"ref.shapeit_all.{i}.yellow" 


    gwf.target(
        name=f'Reel_Het_{i}',
        inputs=[Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        outputs=[Folder_Pi+f"ref.shapeit_all.{i}.yellow.het"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << "vcftools --vcf "+Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf --het --out "+Folder_Pi+f"ref.shapeit_all.{i}.yellow" 


    gwf.target(
        name=f'Reel_Length_{i}',
        inputs=[],
        outputs=[Folder_Pi+f"ref.shapeit_all.{i}.yellow.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << (
    "bcftools query -f '%CHROM\t%POS\n' " + Folder_BCF + f"ref.shapeit_all.{i}.yellow.bcf | "
    "sort -k1,1 -k2,2n | "
    "awk '{{max[$1]=$2}} END {{for (chr in max) print chr, max[chr]}}' | "
    "sort > " + Folder_Pi + f"ref.shapeit_all.{i}.yellow.txt"
)