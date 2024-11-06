import os
import csv
from time import perf_counter


def get_data(path_file: str) -> list[tuple]:
    with open(path_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        data, shares = [], []
        for line in reader:
            cost = float(line[1])
            perf = cost * float(line[2].replace("%", "")) / 100
            if line[0] not in shares and cost > 0 and perf > 0:
                data.append((line[0], cost, perf))
                shares.append(line[0])
        return data


def user_selection():
    csv_files = os.listdir("data/")
    loop = True
    while loop:
        print("\nCsv file list: ")
        for i, file in enumerate(csv_files):
            print(f" {i} -> {file}")
        choice = input("\nSelect csv file number: ")
        invest = input("Enter investment (default=500): ")
        try:
            file = f"data/{csv_files[int(choice)]}"
            max_invest = int(invest) if invest else 500
        except ValueError:
            print("Bad input! Enter a number")
        except IndexError:
            print("File number not in selection !")
        else:
            loop = False
    return file, max_invest


def time_exec(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        time_counter = (perf_counter() - start)*1000
        print(f"Execution time: {round(time_counter, 2)} ms\n")
    return wrapper
