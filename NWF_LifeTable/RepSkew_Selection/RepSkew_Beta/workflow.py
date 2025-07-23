from gwf import Workflow
import itertools

gwf = Workflow()

#Selection_coeff = [0.0,0.00001,0.0001,0.001,0.005,0.01,0.05,0.1]
#Selection_prop = [0.0,0.01,0.05,0.1,0.5]
#Beta = [1,2,3,5,7]
#Num = [k for k in range(1,20)]
Num = [1]
Selection_coeff = [0.001]
Selection_prop = [0.01]
Beta = [1]

parameter_space = itertools.product(Beta,Selection_coeff,Selection_prop,Num)

for beta,scoeff,sprop,i in parameter_space:
    gwf.target(
        name=f'NWFLT_RS_Selec_{beta}_{scoeff*10000}_{sprop}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/RepSkew_Selection/RepSkew_Beta/NWFLT_Pi_RS_Selec{beta},{scoeff},{sprop},{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/RepSkew_Selection/RepSkew_Beta/NWFLT_aod_no_RS_Selec{beta},{scoeff},{sprop},{i}.txt",f'/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/RepSkew_Selection/RepSkew_Beta/NWFLT_RS_Selec_Pop{beta},{scoeff},{sprop},{i}.txt'],
        cores = 1,
        memory = '200Gb',
        walltime = '72:00:00'
        
    ) << f"""
    slim -d NUM={i} -d BETA={beta} -d SELECTION_COEFF={scoeff} -d SELECTION_PROP={sprop} -d SEXRATIO=0.5 -d K=750 -d NTICKS=20000 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/RepSkew_Selection/RepSkew_Beta/NWFLT_RS_Selec.slim
    """
    