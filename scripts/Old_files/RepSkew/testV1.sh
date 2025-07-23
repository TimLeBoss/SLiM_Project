#!/bin/bash
#SBATCH --job-name=RepSkewV3
#SBATCH --output=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/RepSkew_testV3/Pi_output.stdout
#SBATCH --error=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/RepSkew_testV3/Pi_output.stderr
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=1:00:00

for i in {1..100}
do
     slim -d NUM=$i -d BETA=5 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/RepSkew/Test_repSkew.slim
done
