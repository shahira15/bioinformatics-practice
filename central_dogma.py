from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGA")

print("DNA:", dna)

rna = dna.transcribe()
print("RNA:", rna)

protein = dna.translate()
print("Protein:", protein)
