def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    # Slicing works on strings smaller than the slice, e.g. [1,2][:3] == [1,2]
    return scores[0:3]
