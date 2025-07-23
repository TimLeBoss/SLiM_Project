#!/bin/bash
#SBATCH --job-name=Pi_other_migrations
#SBATCH --output=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Other_Migrations/Pi_output.stdout
#SBATCH --error=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Other_Migrations/Pi_output.stderr
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=48:00:00


for p_mig in  0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1
do
    for i in {1..100}
    do
        slim -d NUM=$i -d PROB_MIG=$p_mig /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Pi_Migration/NWF_Mig_Bin.slim
        slim -d NUM=$i -d PROB_MIG=$p_mig /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Pi_Migration/NWF_mig_noAge.slim
        slim -d NUM=$i -d PROB_MIG=$p_mig /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Pi_Migration/NWF_Mig_withfemale.slim
    done
done
