import csv
from time import perf_counter


def get_data(path_file: str) -> list[tuple]:
    with open(path_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        return [
            (line[0],
            float(line[1]),
            round(float(line[2].replace("%", ""))/100 * float(line[1]), 2))
            for line in reader if float(line[1]) > 0
        ]


def time_exec(func):
    def wrapper():
        start = perf_counter()
        func()
        time_counter = (perf_counter() - start)*1000
        print(f"Execution time: {round(time_counter, 2)} ms\n")
    return wrapper
    