def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100

with open("brca1.fasta") as file:
    header = ""
    full_sequence = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            header = line
        else:
            full_sequence += line

    percentage = gc_content(full_sequence)
    print(header)
    print("Total length:", len(full_sequence))
    print("GC content:", round(percentage, 2), "%")
