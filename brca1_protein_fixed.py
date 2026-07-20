from Bio import SeqIO

for record in SeqIO.parse("brca1.fasta", "fasta"):
    seq = record.seq
    start = seq.find("ATG")
    print("First ATG found at position:", start)
    
    coding_seq = seq[start:]
    trim_length = len(coding_seq) - (len(coding_seq) % 3)
    coding_seq = coding_seq[:trim_length]
    
    protein = coding_seq.translate(to_stop=True)
    print("Protein length:", len(protein))
    print("First 60 amino acids:", protein[:60])
