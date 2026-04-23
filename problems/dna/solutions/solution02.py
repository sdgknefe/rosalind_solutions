def dna_counts(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

dna="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

print(dna_counts(dna))