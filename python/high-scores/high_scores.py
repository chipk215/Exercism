def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    score_cnt = len(scores)
    if score_cnt < 3:
        return scores[0:score_cnt]
    else:
        return scores[0:3]
