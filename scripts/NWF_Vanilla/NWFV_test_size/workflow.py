from gwf import Workflow
import itertools

gwf = Workflow()

Lm = [10,20,30,40]
LK = [250,500,750,1000,1250,1500]
Num = [k for k in range(1,501)]
#Num = [1]
#Lm = [10]
#LK = [250]

parameter_space = itertools.product(Lm,LK,Num)

for m,K,i in parameter_space:
    gwf.target(
        name=f'NWFV_Size_m_{m}_K_{K}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWFV_test_size/NWFV_size_K_{K}_m_{m}_{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '05:00:00'
        
    ) << f"""
    slim -d NUM={i} -d SEXRATIO={0.5} -d K={K} -d m={m} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWFV_test_size/NWFV_test_size.slim
    """