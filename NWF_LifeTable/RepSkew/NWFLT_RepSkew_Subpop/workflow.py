from gwf import Workflow
import itertools

gwf = Workflow()


Beta = [1,2,5,10,20,40]
Num = [k for k in range(1,50)]
#Num = [1]
#Beta = [2]

parameter_space = itertools.product(Beta,Num)

for beta,i in parameter_space:
    gwf.target(
        name=f'NWFLT_RepSkew_Beta_SubPop_{beta}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/RepSkew/NWFLT_RepSkew_Subpop/NWFLT_Pi_RepSkew_Subpop_Beta{beta},{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/RepSkew/NWFLT_RepSkew_Subpop/NWFLT_aod_no_RepSkew_Subpop_Beta{beta},{i}.txt"],
        cores = 1,
        memory = '20Gb',
        walltime = '20:00:00'
        
    ) << f"""
    slim -d NUM={i} -d BETA={beta} -d SEXRATIO=0.5 -d K=50 -d Npop=15 -d PROB_MIG=1.0 -d NTICKS=20000 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/RepSkew/NWFLT_RepSkew_Subpop/NWFLT_RepSkew_Beta_subpop.slim
    """
    