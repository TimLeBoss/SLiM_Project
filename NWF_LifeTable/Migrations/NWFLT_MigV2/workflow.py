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
        name=f'NWFLT_MigV2_star_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_subpop_star_Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d SEXRATIO=0.5 -d K=50 -d NTICKS=60000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_MigV2_star.slim
    """
    
    gwf.target(
        name=f'NWFLT_MigV2_circle_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_subpop_circle_Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d K=50 -d NTICKS=20000 -d SEXRATIO=0.5 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_MigV2_circle.slim
    """

    gwf.target(
        name=f'NWFLT_MigV2_stepstone_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_MigV2_stepstone{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d K=50 -d NTICKS=20000 -d SEXRATIO=0.5 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Migrations/NWFLT_MigV2/NWFLT_MigV2_stepstone.slim
    """