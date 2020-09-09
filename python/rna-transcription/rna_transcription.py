
dna_to_rna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    result = ''
    for letter in dna_strand:
        result += dna_to_rna[letter]

    return result
