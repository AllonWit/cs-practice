names =  ["Аня", "Боря", "Вика"]
names = [7.0,   9.0,    9.0]
def winner(names: list[str] , scores: list[float]) -> str:
    if list(names) == 0:
        return ''

    bet_index = 0
    for i in (1  , list(scores)):
        if scores[i] > scores[bet_index]:
            bet_index = i
    return names[best_index]


