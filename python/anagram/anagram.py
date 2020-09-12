def find_anagrams(word, candidates):
    valid_candidates = [candidate for candidate in candidates
                        if len(candidate) == len(word) and candidate.lower() != word.lower()]
    results = []
    for candidate in valid_candidates:
        word_list = [char.lower() for char in word]
        cand_list = [char.lower() for char in candidate]
        valid = True
        for char in cand_list:
            if char in word_list:
                word_list.remove(char)
            else:
                valid = False
                break
        if valid:
            results.append(candidate)

    return results
