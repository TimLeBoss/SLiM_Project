from gwf import Workflow
import itertools

gwf = Workflow()

SexRatio = [0.25,0.3,0.4,0.5,0.6,0.7,0.75]
Num = [k for k in range(1,101)]

parameter_space = itertools.product(SexRatio,Num)

for sr,i in parameter_space:
    gwf.target(
        name=f'PI_NWFLT_SexRatio_{sr}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Pi_WF_NWFLT/NWF_LT_SEXRATIO{sr},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d SEXRATIO={sr} -d K=750 -d NTICKS=60000 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Pi_WF_NWFLT/NWF_LT_SexRatio.slim
    """

    gwf.target(
        name=f'PI_WF_LT_SexRatio_{sr}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Pi_WF_NWFLT/WF_SexRatio{sr},{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d SEXRATIO={sr} -d K=750 -d NTICKS=20000 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Pi_WF_NWFLT/WF_SexRatio.slim
    """