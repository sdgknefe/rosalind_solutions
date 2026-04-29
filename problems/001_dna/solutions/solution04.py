
def dna_count(s):
    a = g = c = t = 0

    for nuc in s:
        if nuc == "A":
            a += 1
        elif nuc == "G":
            g += 1
        elif nuc == "C":
            c += 1
        elif nuc == "T":
            t += 1
    
    return a, c, g, t

dna= "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

print(dna_count(dna))