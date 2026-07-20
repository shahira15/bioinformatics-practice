sequences = ["ATGCGTACGTTAGCGCGCTA", "GGGCCCAAATTTGGGCCC", "ATATATATGCGC"]

for seq in sequences:
    length = len(seq)
    gc_count = seq.count("G") + seq.count("C")
    gc_percentage = (gc_count / length) * 100
    print(seq, "-> GC content:", round(gc_percentage, 2), "%")
