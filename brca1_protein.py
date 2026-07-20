from Bio import SeqIO

for record in SeqIO.parse("brca1.fasta", "fasta"):
    print("ID:", record.id)
    print("DNA length:", len(record.seq))
    
    protein = record.seq.translate()
    print("Protein length:", len(protein))
    print("First 60 amino acids:", protein[:60])
