from gwf import Workflow
import itertools
import os

gwf = Workflow()

NTicks = [1000,5000,10000,20000,50000]
Num = [k for k in range(1,501)]
#NTicks = [20000]
#Num = [1]

parameter_space = itertools.product(NTicks,Num)

for nt,i in parameter_space:
    gwf.target(
        name=f'NWFV_Pop10x50_NTicks_{nt}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Pop10x50_NWFV/NWFV_Pop10x50_NTicks{nt},{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '03:00:00',
        
    ) << f"""
    slim -d NUM={i} -d NTICKS={nt} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Pop10x50_NWFV/NWFV_Pop10x50.slim
    """