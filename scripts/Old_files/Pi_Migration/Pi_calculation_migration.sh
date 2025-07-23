#!/bin/bash
#SBATCH --job-name=Pi_migration
#SBATCH --output=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/PI_Migration/Pi_output.stdout
#SBATCH --error=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/PI_Migration/Pi_output.stderr
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=48:00:00


for p_mig in  0.7 0.75 0.8 0.85 0.9 0.95 1
do
    for i in {1..500}
    do
        slim -d NUM=$i -d PROB_MIG=$p_mig /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Pi_Migration/NWF_Migration.slim
    done
done
