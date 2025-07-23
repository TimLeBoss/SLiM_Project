from gwf import Workflow
import itertools

gwf = Workflow()
Folder_BCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Anubis/BCF_Files/"
Folder_VCF_SNP = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Anubis/VCF_Files_SNP/"
Folder_VCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Anubis/VCF_Files/"
Folder_Pi = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/Anubis/"
Folder_output = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/"
Folder_Fasta = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Anubis/Fasta_Files_format/"
Folder_script = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Reel_Data/Anubis/"
#Chr = [i for i in range (1,22)]
Chr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
#Chr = [1]
Length = []
File = Folder_output+"length_line.txt"
Text = open(File, 'r')
Values = Text.read().split()
for j in range (0,43,2):
    Length.append(float(Values[j+1]))
Text.close()

for i in Chr:

    gwf.target(
        name=f'Reel_VCF_Anub_{i}',
        inputs=[f"{Folder_BCF}ref.shapeit_all.{i}.anubis.bcf"],
        outputs=[Folder_VCF+f"ref.shapeit_all.{i}.anubis.recode.vcf"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << "vcftools --bcf "+Folder_BCF+f"ref.shapeit_all.{i}.anubis.bcf --recode --out "+Folder_VCF+f"ref.shapeit_all.{i}.anubis" 
    
    gwf.target(
        name=f'Reel_VCF_SNP_Anub_{i}',
        inputs=[Folder_VCF+f"ref.shapeit_all.{i}.anubis.recode.vcf"],
        outputs=[Folder_VCF_SNP+f"ref.shapeit_all.{i}.anubis.recode.vcf"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << f"python {Folder_script}Only_SNP_VCF.py {i}"

    gwf.target(
        name=f'Reel_SLiM_Pi_Anub{i}',
        inputs=[Folder_Fasta+f"{i}.fasta",Folder_VCF +f"ref.shapeit_all.{i}.anubis.recode.vcf"],
        outputs=[Folder_Pi+f"reel_pi_SLiM_{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '04:00:00',
        queue = "short,standard"

         
    ) << f"slim -d NUM={i} -d Length={int(Length[i-1])} -d NIND=182 "+Folder_script+"Pi_calculation_ReelData_Yellow.slim"