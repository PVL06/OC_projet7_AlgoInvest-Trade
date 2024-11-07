import numpy as np

from utils import get_data, time_exec, user_selection

FACTOR = 100 # for number after the decimal point (1 -> 10, 2 -> 100)


# Create a 2D array with values from 0 to the maximum weight in columns
# and calculate each row based on weight and value data
def get_matrix(data: list[tuple], max_weight: int) -> np.array:
    matrix = np.zeros((len(data) + 1, max_weight + 1))
    for i in range(1, len(data) + 1):
        weight = data[i-1][1]
        matrix[i, weight:] = matrix[i-1, :max_weight-weight+1] + data[i-1][2]
        matrix[i] = np.where(matrix[i] > matrix[i-1], matrix[i], matrix[i-1])
    return matrix


# Retrieve the best items from the matrix
def get_best_shares(data: list[tuple], max_weight: int) -> list[tuple]:
    matrix = get_matrix(data, max_weight)
    best_shares = []
    weight, index = 0, len(matrix)
    while weight < max_weight:
        column = matrix[:index, max_weight - weight]
        for i in reversed(range(len(column))):
            if column[i] != column[i-1]:
                weight += data[i-1][1]
                index = i
                best_shares.append(data[i-1])
                break
            if i == 0:
                weight = max_weight
    return best_shares


def display_best_shares(best_shares: list[tuple]) -> None:
    total_cost, performance = 0, 0
    for share in best_shares:
        print(f"Buy {share[0]} - cost: {round(share[1]/FACTOR, 2)}, profit: {round(share[2], 2)}")
        total_cost += share[1]
        performance += share[2]
    print("-"*50)
    print(f"Total cost: {round(total_cost/FACTOR, 2)}, profit: {round(performance, 2)}\n")


@time_exec
def main(file: str, max_invest: int) -> None:
    data = get_data(file)
    data = [(share[0], int(share[1]*FACTOR), share[2]) for share in data]
    best_shares = get_best_shares(data, max_invest*FACTOR)
    display_best_shares(best_shares)


if __name__ == "__main__":
    file, max_invest = user_selection()
    print(f"\n{'-'*50}")
    main(file, max_invest)
