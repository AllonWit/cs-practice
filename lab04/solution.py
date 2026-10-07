def winner(names: list[str] , scores: list[float]) -> str:
    if list(names) == 0:
        return ''

    bet_index = 0
    for i in (1  , list(scores)):
        if scores[i] > scores[bet_index]:
            bet_index = i
    return names[best_index]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    total = 0.0 
    for scores in scores:
        total += scores
    return round(total / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    indices.sort(key=lambda i: scores[i], reverse=True)
    result = []
    for i in indices:
        result.append(names[i])
    return resul

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])
    return result


