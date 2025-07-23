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
        name=f'WF_HetPiWa_NTicks_{nt}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/WF_Vanilla/WF_Het_Pi_Wa/WF_HetPiWa_Ticks{nt},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00',
        
    ) << f"""
    slim -d NUM={i} -d NTICKS={nt} -d SEXRATIO=0.5 -d K=750 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/WF_Vanilla/WF_Het_Pi_Wa/WF_Pi_Watterson.slim
    """