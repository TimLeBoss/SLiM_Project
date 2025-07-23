from gwf import Workflow
import itertools
import os

gwf = Workflow()

FOLDER_out = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Hybridization/2SLiM_Files/"
FOLDER_in = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Hybridization/2SLiM_Files/"
NBP = 20000
sr = 0.5
K = 750
m = 40
#TSEP = [0,5000,10000,15000,20000,25000,30000]
#NMIG = [1,10,50,100,300]
#Num = [k for k in range(1,21)]
TSEP = [1000]
NMIG = [1]
Num = [1]

for i in Num:
    gwf.target(
        name=f'NWFLT_Hyb_BP_{i}',
        inputs=[],
        outputs=[FOLDER_out+f"NWFLT_Hyb_BP{i}.txt",FOLDER_out+f"NWFLT_Hyb_Pop_BP{i}.txt"],
        cores = 1,
        memory = '10Gb',
        walltime = '10:00:00',
        
    ) << f"slim -d NUM={i} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_BurningPeriod.slim"

    
    gwf.target(
        name=f'NWFLT_Hyb_NBP_{i}',
        inputs=[FOLDER_out+f"NWFLT_Hyb_Pop_BP{i}.txt"],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_NBP{i}.txt",],
        cores = 1,
        memory = '40Gb',
        walltime = '10:00:00',
        
    ) << f"slim -d NUM={i} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_NextBP.slim"

parameter_space = itertools.product(TSEP,NMIG,Num)

for tsep,nmig,i in parameter_space:

    gwf.target(
        name=f'NWFLT_Hyb_OM_{tsep}_{nmig}_{i}',
        inputs=[FOLDER_out+f"NWFLT_Hyb_Pop_BP{i}.txt"],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_OM{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_OM{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '72:00:00',
        
    ) << f"slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_OnlyMales.slim"
    
    
    gwf.target(
        name=f'NWFLT_Hyb_OF_{tsep}_{nmig}_{i}',
        inputs=[FOLDER_out+f"NWFLT_Hyb_Pop_BP{i}.txt"],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_OF{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_OF{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '72:00:00',
        
    ) << f'slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} '+FOLDER_in+'NWFLT_Hyb_OnlyFemales.slim'


    gwf.target(
        name=f'NWFLT_Hyb_WMF_{tsep}_{nmig}_{i}',
        inputs=[FOLDER_out+f"NWFLT_Hyb_Pop_BP{i}.txt"],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_WMF{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_WMF{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '72:00:00',
        
    ) << f"slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_WithMalesFemales.slim"