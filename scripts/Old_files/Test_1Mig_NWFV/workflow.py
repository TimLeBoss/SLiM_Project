from gwf import Workflow
import itertools

gwf = Workflow()

P_Mig = [0.0]+[k/20 for k in range(1,20)]+[1.0]
Num = [k for k in range(1,501)]
#Num = [1]
#P_Mig = [0.0]

parameter_space = itertools.product(P_Mig,Num)

for pmig,i in parameter_space:
    gwf.target(
        name=f'NWFV_1Migration_{pmig}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_1Mig_NWFV/NWFV_circle_1Migration{pmig},{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_1Mig_NWFV/NWFV_star_1Migration{pmig},{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '01:00:00'

    ) << f"""
    slim -d NUM={i} -d PROB_MIG={pmig} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_1Mig_NWFV/NWFV_1Mig_circle.slim
    slim -d NUM={i} -d PROB_MIG={pmig} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_1Mig_NWFV/NWFV_1Mig_star.slim
    """