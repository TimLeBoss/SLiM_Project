from gwf import Workflow
import itertools
import os

gwf = Workflow()

SexRatio = [0.25,0.3,0.4,0.5,0.6,0.7,0.75]
P_Mig = [0]+[k/20 for k in range(1,20)]+[1]
Num = [k for k in range(1,101)]

parameter_space = itertools.product(SexRatio,P_Mig,Num)

for sr, pmig,i in parameter_space:
    gwf.target(
        name=f'NWFLT_Sexratio_{sr}_Migration_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Migration_SexRatio/Pi_Prob_Mig{pmig},SexRatio{sr},{i}.txt"],
        cores = 1,
        memory = '2g',
        walltime = '00:01:00',
        
    ) << f"""
    slim -d NUM={i} -d SEXRATIO={sr} -d PROB_MIG={pmig} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Migration_SexRatio/Migration_SexRatio.slim
    """