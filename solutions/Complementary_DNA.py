"""
7 kyu: Complementary DNA
http://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
"""
def DNA_strand(dna):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([complements[c] for c in dna])


print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))