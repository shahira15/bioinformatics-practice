sequence = "ATGCGTACGTTAGCGCGCTA"

a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)

total_length = len(sequence)
gc_count = g_count + c_count
gc_percentage = (gc_count / total_length) * 100

print("GC content:", gc_percentage, "%")
