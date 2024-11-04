import os
import copy
import math

import numpy as np

from utils import get_data, time_exec, user_selection


def get_new_array(last_array: np.array, weight: float, value: float) -> np.array:
    new_array = copy.deepcopy(last_array)
    new_array[weight:] = last_array[:len(last_array[weight:])] + value
    return np.where(last_array > new_array, last_array, new_array)


def get_matrix(data: list[tuple], max_weight: int) -> np.array:
    matrix = np.array([[0]*(max_weight+1)], float)
    for i in range(len(data)):
        array = get_new_array(matrix[i], math.ceil(data[i][1]), data[i][2])
        matrix = np.append(matrix, [array], axis=0)
    return matrix


def get_best_items(data: list[tuple], max_weight: int) -> list[str]:
    matrix = get_matrix(data, max_weight)
    best_share = []
    weight, index = 0, len(matrix)
    while weight < max_weight:
        column = matrix[:index, max_weight - math.ceil(weight)]
        for i in reversed(range(len(column))):
            if column[i] != column[i-1]:
                weight += data[i-1][1]
                index = i
                best_share.append(data[i-1][0])
                break
            if i == 0:
                weight = max_weight
    return best_share


def display_best_share(data: list[tuple], best_shares: list[str]) -> None:
    total_cost, performance = 0, 0
    for share in data:
        if share[0] in best_shares:
            total_cost += share[1]
            performance += share[2]
            print(f"Buy {share[0]} - cost: {round(share[1], 2)}, profit: {round(share[2],2 )}")
    print("-"*50)
    print(f"Total cost: {round(total_cost, 2)}, profit: {round(performance, 2)}\n")


@time_exec
def main(file: str, max_invest: int) -> None:
    data = get_data(file)
    best_share = get_best_items(data, max_invest)
    display_best_share(data, best_share)


if __name__ == "__main__":
    file, max_invest = user_selection()
    print(f"\n{'-'*50}")
    main(file, max_invest)
