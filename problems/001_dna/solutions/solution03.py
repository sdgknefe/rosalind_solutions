def dna_count(s):
    result={
        "A": 0, "C": 0, "G": 0, "T": 0 
    }

    for nucleotit in s:
        result[nucleotit] +=1 

    return result

dna="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

print(dna_count(dna))
