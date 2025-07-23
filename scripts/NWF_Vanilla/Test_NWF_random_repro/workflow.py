from gwf import Workflow
import itertools

gwf = Workflow()

SexRatio = [0.25,0.5,0.75]
Num = [k for k in range(1,501)]
#Num = [1]
#SexRatio = [0.25]

parameter_space = itertools.product(SexRatio,Num)

for sr,i in parameter_space:
    gwf.target(
        name=f'PI_WF_NWFRR_SexRatio_{sr}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_NWF_random_repro/NWF_RandomRepro_SexRatio{sr},{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_NWF_random_repro/WF_SexRatio{sr},{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '01:00:00'
        
    ) << f"""
    slim -d NUM={i} -d SEXRATIO={sr} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_NWF_random_repro/NWF_random_repro.slim
    slim -d NUM={i} -d SEXRATIO={sr} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_NWF_random_repro/WF_SexRatio.slim
    """