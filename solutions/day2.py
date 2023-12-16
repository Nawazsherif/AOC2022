import operator
from functools import reduce
from typing import List

shape_vs_value_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win_map = {
    "A": 2,
    "B": 3,
    "C": 1,
}
lose_map = {
    "A": 3,
    "B": 1,
    "C": 2,
}


def calculate_score1(match_input: str):
    opponent_shape, strategical_shape = match_input.rstrip().split(" ")
    if shape_vs_value_map[strategical_shape] == shape_vs_value_map[opponent_shape]:
        return shape_vs_value_map[strategical_shape] + 3
    elif opponent_shape == "A" and strategical_shape == "Y":
        return shape_vs_value_map[strategical_shape] + 6
    elif opponent_shape == "B" and strategical_shape == "Z":
        return shape_vs_value_map[strategical_shape] + 6
    elif opponent_shape == "C" and strategical_shape == "X":
        return shape_vs_value_map[strategical_shape] + 6
    return shape_vs_value_map[strategical_shape]


def calculate_score2(match_input: str):
    opponent_shape, decision = match_input.rstrip().split(" ")
    if decision == "Y":
        return shape_vs_value_map[opponent_shape] + 3
    elif decision == "Z":
        return win_map[opponent_shape] + 6
    return lose_map[opponent_shape]


def calculate_score_for_rock_paper_scissors():
    file = open("../inputs/day2.bat")
    data: List[str] = file.readlines()
    score_for_all_rounds = [calculate_score2(match_input) for match_input in data]
    print(score_for_all_rounds)
    total_score = reduce(operator.add, score_for_all_rounds)
    print(total_score)


if __name__ == '__main__':
    calculate_score_for_rock_paper_scissors()
