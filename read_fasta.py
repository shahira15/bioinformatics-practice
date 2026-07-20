with open("sequences.fasta") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            print("Header:", line)
        else:
            print("Sequence:", line)
