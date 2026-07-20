from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("brca1.fasta", "fasta"):
    print("ID:", record.id)
    print("Description:", record.description)
    print("Length:", len(record.seq))
    print("GC content:", round(gc_fraction(record.seq) * 100, 2), "%")

