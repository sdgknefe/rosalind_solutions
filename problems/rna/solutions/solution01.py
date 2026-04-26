def dna_to_rna(dna):    
    
    dna = dna.replace("T", "U")
    
    return dna


dna = "GATGGAACTTGACTACGTAAATT"

print(dna_to_rna(dna))
