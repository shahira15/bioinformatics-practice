def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100

with open("sequences.fasta") as file:
    header = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            header = line
        else:
            percentage = gc_content(line)
            print(header, "-> GC content:", round(percentage, 2), "%")
