# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
# and carries the "instructions" for the development and functioning of living organisms.
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA; you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def DNA_strand(dna):
    dna_list = []
    dna_list[:] = dna
    for i in range(0, len(dna_list)):
        if dna_list[i] == "A":
            dna_list[i] = "T"
        elif dna_list[i] == "T":
            dna_list[i] = "A"
        if dna_list[i] == "C":
            dna_list[i] = "G"
        elif dna_list[i] == "G":
            dna_list[i] = "C"
    dna_string = ''.join(dna_list)
    return dna_string


DNA_strand("AAAA")
DNA_strand("ATTGC")
DNA_strand("GTAT")
