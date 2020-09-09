codon_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}


def proteins(strand):
    n = 3
    codons = [(strand[i:i+n]) for i in range(0, len(strand), n)]
    result = []
    for codon in codons:
        protein = codon_protein[codon]
        if protein == 'STOP':
            break
        else:
            result.append(protein)
    return result



