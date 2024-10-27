import copy

import numpy as np

from csv_reader import get_data


def get_new_array(last_array, weight, value):
    new_array = copy.deepcopy(last_array)
    new_array[weight:] = last_array[:len(last_array[weight:])] + value
    return np.where(last_array > new_array, last_array, new_array)


def get_matrix(data, max_weight):
    matrix = np.array([[0]*(max_weight+1)], float)
    for i in range(len(data)):
        array = get_new_array(matrix[i], round(data[i][1]), data[i][2])
        matrix = np.append(matrix, [array], axis=0)
    return matrix


def get_best_items(data: list, max_weight):
    matrix = get_matrix(data, max_weight)
    items = []
    weight, index = 0, len(matrix)
    while weight < max_weight:
        columns = matrix[:index, max_weight - weight]
        for i in reversed(range(len(columns))):
            if columns[i] != columns[i-1]:
                weight += round(data[i-1][1])
                index = i
                items.append(data[i-1][0])
                break
            if i == 0:
                weight = max_weight
    return items


if __name__ == "__main__":
    file = "data/dataset2.csv"
    max = 500
    data = get_data(file)
    res = get_best_items(data, max)
    print(res)


