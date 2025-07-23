from gwf import Workflow
import itertools
import os

gwf = Workflow()

NTicks = [1000,5000,10000,20000,50000]
Num = [k for k in range(1,101)]
#NTicks = [1000]
#Num = [1]

parameter_space = itertools.product(NTicks,Num)

for nt,i in parameter_space:
    gwf.target(
        name=f'WF_Pop15x50_NTicks_{nt}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/WF_Vanilla/Test_Pop15x50_WF/WF_Pop15x50_Ticks{nt},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '05:00:00',
        
    ) << f"""
    slim -d NUM={i} -d NTICKS={nt} -d SEXRATIO=0.5 -d Npop=15 -d K=50 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/WF_Vanilla/Test_Pop15x50_WF/WF_Pop15x50.slim
    """