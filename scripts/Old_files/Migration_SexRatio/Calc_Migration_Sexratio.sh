#!/bin/bash
#SBATCH --job-name=Pi_Mig_SexRatio
#SBATCH --output=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Migration_SexRatio/Pi_output.stdout
#SBATCH --error=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Migration_SexRatio/Pi_output.stderr
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=24:00:00

for sexratio in 0.25 0.3 0.4 0.5 0.6 0.7 0.75
    do
    for p_mig in 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5
    do
        for i in {1..100}
        do
            slim -d NUM=$i -d PROB_MIG=$p_mig -d SEXRATIO=$sexratio /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Migration_SexRatio/Migration_SexRatio.slim
        done
    done
done