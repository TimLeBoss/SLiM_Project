from gwf import Workflow
import itertools

gwf = Workflow()

Pmig = [k/20 for k in range(1,20)]+[1.0]
Num = [k for k in range(1,101)]
#Num = [1]
#Pmig = [0.25]

parameter_space = itertools.product(Pmig,Num)

for pmig,i in parameter_space:
    gwf.target(
        name=f'NWF_1MigV2_star_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_Vanilla/Migrations/NWFV_1MigV2/NWFV_star_1Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d SEXRATIO=0.5 -d K=50 -d NTICKS=20000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_Vanilla/Migrations/NWFV_1MigV2/NWFV_1MigV2_star.slim
    """

    gwf.target(
        name=f'NWF_1MigV2_circle_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_Vanilla/Migrations/NWFV_1MigV2/NWFV_circle_1Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d SEXRATIO=0.5 -d K=50 -d NTICKS=20000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_Vanilla/Migrations/NWFV_1MigV2/NWFV_1MigV2_circle.slim
    """
    