from gwf import Workflow
import itertools

gwf = Workflow()

gwf.target(
    name=f'NWFV_AoD_NOff_AD',
    inputs=[],
    outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFV_aod_no.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFV_ad.txt"],
    cores = 1,
    memory = '10Gb',
    walltime = '05:00:00'
        
) << f"""
slim -d K=750 -d SEXRATIO=0.5 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/NWF_AoD_NOff_AD/NWF_Van_AoD_NOff_AD.slim
"""


gwf.target(
    name=f'NWFFC_AoD_NOff_AD',
    inputs=[],
    outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFFC_aod_no.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFFC_ad.txt"],
    cores = 1,
    memory = '10Gb',
    walltime = '05:00:00'
        
) << f"""
slim -d K=750 -d SEXRATIO=0.5 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/NWF_AoD_NOff_AD/NWF_FC_test_aad_no.slim
"""


gwf.target(
    name=f'NWFLT_AoD_NOff_AD',
    inputs=[],
    outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFLT_aod_no.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/NWF_LifeTable/NWF_AoD_NOff_AD/NWFLT_ad.txt"],
    cores = 1,
    memory = '10Gb',
    walltime = '05:00:00'
        
) << f"""
slim -d K=750 -d SEXRATIO=0.5 /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/NWF_LifeTable/NWF_AoD_NOff_AD/NWF_LT_AoD_NOff.slim
"""