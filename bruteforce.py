from typing import Generator

from csv_reader import get_data

FILE = "data/Liste_actions_P7.csv"
MAX_INVEST = 500

"""
O(n * 2^n)
"""

def get_combinations(n: int) -> Generator:
    for i in range(2**n - 1):
        yield bin(i)[2:].zfill(n)


def get_best_combination(combinations: Generator, data: list[tuple]) -> str:
    best_perf, best_combination = 0, ""
    for combination in combinations:
        perf, invest= 0, 0
        for i, buy in enumerate(combination):
            if buy == "1":
                invest += data[i][1]
                perf += data[i][2]

        if invest <= MAX_INVEST and perf > best_perf:
            best_perf = perf
            best_combination = combination
    return best_combination


def display_results(data: list[tuple], best_combination: str) -> None:
    total_cost, performance = 0, 0
    for index, buy in enumerate(best_combination):
        if buy == "1":
            print(f"Buy {data[index][0]} - cost: {data[index][1]}, profit: {data[index][2]}")
            total_cost += data[index][1]
            performance += data[index][2]
    print("-"*50)
    print(f"Total cost: {total_cost}, profit: {round(performance, 2)}\n")


if __name__ == "__main__":
    data = get_data(FILE)
    combinations = get_combinations(len(data))
    best_combination = get_best_combination(combinations, data)
    display_results(data, best_combination)