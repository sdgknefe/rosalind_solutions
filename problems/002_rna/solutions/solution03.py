dna = "GATGGAACTTGACTACGTAAATT"

rna = "".join(["U" if base == "T" else base for base in dna])

print(rna)