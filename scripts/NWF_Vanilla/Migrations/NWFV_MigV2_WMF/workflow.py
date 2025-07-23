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
        name=f'NWF_MigV2_WMF_star_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_Vanilla/Migrations/NWFV_MigV2_WMF/NWFV_WMF_star_Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d K=50 -d NTICKS=20000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_Vanilla/Migrations/NWFV_MigV2_WMF/NWFV_MigV2_WMF_star.slim
    """

    gwf.target(
        name=f'NWF_MigV2_WMF_circle_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_Vanilla/Migrations/NWFV_MigV2_WMF/NWFV_WMF_circle_Mig{pmig},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} -d K=50 -d NTICKS=20000 -d Npop=15 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_Vanilla/Migrations/NWFV_MigV2_WMF/NWFV_MigV2_WMF_circle.slim
    """