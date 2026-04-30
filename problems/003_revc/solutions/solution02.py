def revc(dna):
    
    result = []

    for base in dna:
        if base == "A":
            result.append("T")
        elif base == "T":
            result.append("A")
        elif base == "G":
            result.append("C")
        else:
            result.append("G")

    return "".join(result[::-1])

dna = "AAAACCCGGT"

print(revc(dna))

