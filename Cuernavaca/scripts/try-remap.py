import remap

# load the reference sequence
with open('../data/Zika-reference.fa', 'rU') as f:
    refseq = ''
    for line in f:
        if line.startswith('>'):
            continue
        refseq += line.strip('\n')

handle = open('../sandbox/local.sam', 'rU')

pileup, counts = remap.sam_to_pileup(handle)
conseqs = remap.pileup_to_conseq(pileup, 10)

remap.update_reference(refseq, conseqs.values()[0])


print conseq
