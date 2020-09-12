def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands have different lengths.")

    differences = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            differences += 1

    return differences


# saw this via google and was interested in zip
def distance_with_zip(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands have different lengths.")

    return sum(s1 != s2 for s1, s2 in zip(strand_a, strand_b))



