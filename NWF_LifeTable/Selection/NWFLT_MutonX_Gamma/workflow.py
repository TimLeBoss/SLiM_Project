from gwf import Workflow
import itertools

gwf = Workflow()

#Selection_coeff = [0.01,0.02,0.05,0.1,0.2,0.5]
#Selection_prop = [0.001,0.01,0.1,1.0]
Selection_coeff = [0.0,0.00001,0.00005,0.0001,0.0005,0.001,0.005,0.01,0.02,0.05,0.1]
Selection_prop = [0.0,0.01,0.03,0.05,0.07,0.09,0.1,0.2,0.3,0.4,0.5]
Num = [k for k in range(1,50)]
#Num = [1]
#Selection_coeff = [0.1]
#Selection_prop = [0.01]

parameter_space = itertools.product(Selection_coeff,Selection_prop,Num)

for scoeff,sprop,i in parameter_space:
    gwf.target(
        name=f'NWFLT_Selec_XGamma_{scoeff*10000}_{sprop}_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Selection/NWFLT_MutonX_Gamma/NWFLT_Mut_OnX{scoeff},{sprop},{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Selection/NWFLT_MutonX_Gamma/NWFLT_Mut_OnX_Pop{scoeff},{sprop},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '10:00:00'
        
    ) << f"""
    slim -d NUM={i} -d SELECTION_COEFF={scoeff} -d SELECTION_PROP={sprop} -d SEXRATIO=0.5 -d K=750 -d NTICKS=60000 -d m=40 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Selection/NWFLT_MutonX_Gamma/NWFLT_MutonX_Gamma.slim
    """
    