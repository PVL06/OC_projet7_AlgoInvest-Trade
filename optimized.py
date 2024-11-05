import numpy as np

from utils import get_data, time_exec, user_selection

FACTOR = 100 # for number after the decimal point (1 -> 10, 2 -> 100) 

def get_matrix(data: list[tuple], max_weight: int) -> np.array:
    matrix = np.zeros((len(data) + 1, max_weight + 1))
    for i in range(1, len(data) + 1):
        weight = data[i-1][1]
        matrix[i, weight:] = matrix[i-1, :max_weight-weight+1] + data[i-1][2]
        matrix[i] = np.where(matrix[i] > matrix[i-1], matrix[i], matrix[i-1])
    return matrix


def get_best_share(data: list[tuple], max_weight: int) -> list[str]:
    matrix = get_matrix(data, max_weight)
    best_share = []
    weight, index = 0, len(matrix)
    while weight < max_weight:
        column = matrix[:index, max_weight - weight]
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
            print(f"Buy {share[0]} - cost: {round(share[1]/FACTOR, 2)}, profit: {round(share[2],2 )}")
    print("-"*50)
    print(f"Total cost: {round(total_cost/FACTOR, 2)}, profit: {round(performance, 2)}\n")


@time_exec
def main(file: str, max_invest: int) -> None:
    data = get_data(file)
    data = [(share[0], int(share[1]*FACTOR), share[2]) for share in data]
    best_share = get_best_share(data, max_invest*FACTOR)
    display_best_share(data, best_share)


if __name__ == "__main__":
    file, max_invest = user_selection()
    print(f"\n{'-'*50}")
    main(file, max_invest)
