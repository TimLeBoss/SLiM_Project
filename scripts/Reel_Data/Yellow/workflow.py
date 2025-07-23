from gwf import Workflow
import itertools

gwf = Workflow()
Folder_BCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/BCF_Files/"
Folder_VCF_SNP = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/VCF_Files_SNP/"
Folder_VCF = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/VCF_Files/"
Folder_Pi = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/Yellow/"
Folder_output = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Reel_Data/"
Folder_Fasta = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/Fasta_Files_format/"
Folder_script = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Reel_Data/Yellow/"
Chr = [i for i in range (1,22)]
#Chr = [i for i in range (1,21)]
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
        name=f'Reel_VCF_{i}',
        inputs=[f"{Folder_BCF}ref.shapeit_all.{i}.yellow.bcf"],
        outputs=[Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << "vcftools --bcf "+Folder_BCF+f"ref.shapeit_all.{i}.yellow.bcf --recode --out "+Folder_VCF+f"ref.shapeit_all.{i}.yellow" 
    
    gwf.target(
        name=f'Reel_VCF_SNP_{i}',
        inputs=[Folder_VCF+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        outputs=[Folder_VCF_SNP+f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        cores = 1,
        memory = '500Mb',
        walltime = '04:00:00',
        queue = "short,standard"
             
    ) << f"python {Folder_script}Only_SNP_VCF.py {i}"

    gwf.target(
        name=f'Reel_SLiM_Pi_{i}',
        inputs=[Folder_Fasta+f"{i}.fasta",Folder_VCF +f"ref.shapeit_all.{i}.yellow.recode.vcf"],
        outputs=[Folder_Pi+f"reel_pi_SLiM_{i}.txt"],
        cores = 1,
        memory = '4Gb',
        walltime = '04:00:00',
        queue = "short,standard"

         
    ) << f"slim -d NUM={i} -d Length={int(Length[i-1])} -d NIND=68 "+Folder_script+"Pi_calculation_ReelData_Yellow.slim"