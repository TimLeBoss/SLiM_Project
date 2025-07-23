from gwf import Workflow
import itertools

gwf = Workflow()


Num = [k for k in range(1,501)]
#Num = [1,2]


parameter_space = itertools.product(Num)

for i in Num:
    gwf.target(
        name=f'NWFVan_Migration_Onlymale_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_circle_Onlymale_{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_star_Onlymale_{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '01:00:00'
        
    ) << f"""
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWF_Van_Migration_circle.slim
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWF_Van_Migration_star.slim
    """

for i in Num:
    gwf.target(
        name=f'NWFVan_Migration_Onlyfemale_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_circle_Onlyfemale_{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_star_Onlyfemale_{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '01:00:00'
        
    ) << f"""
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWFV_Mig_circle_Onlyfemale.slim
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWFV_Mig_star_Onlyfemale.slim
    """

for i in Num:
    gwf.target(
        name=f'NWFVan_Migration_wfemales_{i}',
        inputs=[],
        outputs=[f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_circle_wfemales_{i}.txt",f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/tmp/Test_Migrations_NWFV/NWFV_Mig_star_wfemales_{i}.txt"],
        cores = 1,
        memory = '500Mb',
        walltime = '01:00:00'
        
    ) << f"""
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWFV_Mig_circle_wfemales.slim
    slim -d NUM={i} /mnt/primevo/work/timothe_dandoy/SLiM_Project/scripts/Test_Migrations_NWFV/NWFV_Mig_star_wfemales.slim
    """