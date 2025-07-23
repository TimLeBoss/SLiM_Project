#!/bin/bash
#SBATCH --job-name=RepSkewV3
#SBATCH --output=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/RepSkew_testV3/Pi_output.stdout
#SBATCH --error=/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/RepSkew_testV3/Pi_output.stderr
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=24:00:00

for fpm in 1 2 3 4 5 6 7 8 9 10
do
    for i in {1..500}
    do
        slim -d NUM=$i -d F_P_M=$fpm /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/RepSkew/RepSkew_testV3.slim
    done
done

for Beta in 2 2.5 3 3.5 4 4.5 5 5.5 6 10
do
    for i in {1..500}
    do
        slim -d NUM=$i -d BETA=$Beta /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/RepSkew/Test_repSkew.slim
        slim -d NUM=$i -d BETA=$Beta /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/RepSkew/TestV2_repSkew.slim
    done
done

for i in {1..500}
do
    slim -d NUM=$i /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/RepSkew/TestV0_repSkew.slim
done