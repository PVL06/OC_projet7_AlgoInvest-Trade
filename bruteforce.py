import csv
import os
from typing import Generator

FILE = "Liste_actions_P7.csv"
MAX_INVEST = 500

def get_data(path_file: str) -> list[(str, int, float)]:
    with open(path_file, mode="r") as file:
        reader = csv.reader(file)
        return [(element[0], int(element[1]), int(element[2][:-1])/100 * int(element[1])) for element in list(reader)[1:]]

def get_combinations(n: int) -> Generator:
    for i in range(2**n - 1):
        yield bin(i)[2:].zfill(n)


def get_best_combination(combinations: Generator, data: list[(str, int, float)]) -> list[str]:
    best_perf, best_combination = 0, ""
    for combination in combinations:
        perf, invest= 0, 0
        for i, buy in enumerate(combination):
            if int(buy):
                invest += data[i][1]
                perf += data[i][2]

        if invest <= MAX_INVEST and perf > best_perf:
            best_perf = perf
            best_combination = combination
    return [data[index][0] for index, buy in enumerate(best_combination) if int(buy)]

file = f"{os.getcwd()}/{FILE}"
data = get_data(file)
combinations = get_combinations(len(data))
best_combination = get_best_combination(combinations, data)
print(best_combination)