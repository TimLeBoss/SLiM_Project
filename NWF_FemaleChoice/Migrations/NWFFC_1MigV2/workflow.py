from gwf import Workflow
import itertools

gwf = Workflow()

Pmig = [k/20 for k in range(1,20)]+[1.0]
#Pmig = [k/200 for k in range(1,20)]
Num = [k for k in range(1,101)]
#Num = [1]
#Pmig = [0.25]

parameter_space = itertools.product(Pmig,Num)

for pmig,i in parameter_space:
    gwf.target(
        name=f'NWFFC_1MigV2_star_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_FemaleChoice/Migrations/NWFFC_1MigV2/NWFFC_subpop_star_1Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '24:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d SEXRATIO=0.5 -d K=50 -d NTICKS=20000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_FemaleChoice/Migrations/NWFFC_1MigV2/NWFFC_1MigV2_star.slim
    """
    
    gwf.target(
        name=f'NWFFC_1MigV2_circle_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_FemaleChoice/Migrations/NWFFC_1MigV2/NWFFC_subpop_circle_1Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '24:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d K=50 -d NTICKS=20000 -d SEXRATIO=0.5 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_FemaleChoice/Migrations/NWFFC_1MigV2/NWFFC_1MigV2_circle.slim
    """