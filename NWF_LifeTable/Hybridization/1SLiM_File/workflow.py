from gwf import Workflow
import itertools
import os

gwf = Workflow()

FOLDER_out = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/Hybridization/1SLiM_File/"
FOLDER_in = "/mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/Hybridization/1SLiM_File/"
NBP = 60000
sr = 0.5
K = 750
m = 40
TSEP = [0,5000,10000,15000,20000,25000,30000]
NMIG = [1,10,50,100,300]
Num = [k for k in range(1,21)]
#TSEP = [1000]
#NMIG = [1]
#Num = [1]

parameter_space = itertools.product(TSEP,NMIG,Num)

for tsep,nmig,i in parameter_space:

    gwf.target(
        name=f'NWFLT_Hyb_1File_OM_{tsep}_{nmig}_{i}',
        inputs=[],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_OM{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_OM{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '96:00:00',
        
    ) << f"slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_OM_1File.slim"
    

    gwf.target(
        name=f'NWFLT_Hyb_1File_OF_{tsep}_{nmig}_{i}',
        inputs=[],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_OF{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_OF{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '96:00:00',
        
    ) << f"slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_OF_1File.slim"
    

    gwf.target(
        name=f'NWFLT_Hyb_1File_WMF_{tsep}_{nmig}_{i}',
        inputs=[],
        outputs=[FOLDER_out+f"NWFLT_Hyb_Pi_WMF{tsep},{nmig},{i}.txt",FOLDER_out+f"NWFLT_Hyb_Fst_WMF{tsep},{nmig},{i}.txt"],
        cores = 1,
        memory = '50Gb',
        walltime = '96:00:00',
        
    ) << f"slim -d NUM={i} -d TSEP={tsep} -d NMIG={nmig} -d SEXRATIO={sr} -d K={K} -d m={m} -d NBP={NBP} "+FOLDER_in+"NWFLT_Hyb_WMF_1File.slim"
    