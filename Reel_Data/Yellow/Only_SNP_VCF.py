import sys

vi = sys.argv[1]

vcf_in_path = f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/VCF_Files/ref.shapeit_all.{vi}.yellow.recode.vcf"
vcf_out_path = f"/mnt/primevo/work/timothe_dandoy/SLiM_Project/data/Reel_Amboseli_Yellow/VCF_Files_SNP/ref.shapeit_all.{vi}.yellow.recode.vcf"

with open(vcf_in_path, 'r') as vcf_in, open(vcf_out_path, 'w') as vcf_out:
    for line in vcf_in:
        if line.startswith('#'):
            vcf_out.write(line)
            continue

        fields = line.strip().split('\t')
        ref = fields[3]
        alt = fields[4]

        # Cas de MNPs (multi-nucleotide polymorphisms)
        if ',' in alt:
            alts = alt.split(',')
        else:
            alts = [alt]

        new_alts = []
        write_record = False

        for a in alts:
            if len(ref) == len(a) and len(ref) > 1:
                if ref[0] != a[0] and ref[1:] == a[1:]:
                    # Simplify to SNP
                    new_alts.append(a[0])
                    write_record = True

        if write_record and len(new_alts) == 1:
            fields[3] = ref[0]
            fields[4] = new_alts[0]
            vcf_out.write('\t'.join(fields) + '\n')
