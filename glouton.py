from utils import get_data, time_exec, user_selection


def get_best_shares(data: list[tuple], max_invest: int) -> list[str]:
    data.sort(reverse=True, key= lambda share: share[2]/share[1])
    weight, profit = 0, 0
    for share in data:
        if share[1] + weight < max_invest:
            print(f"Share: {share[0]} - cost: {share[1]}, profit: {round(share[2], 2)}")
            weight += share[1]
            profit += share[2]
    print("-"*50)
    print(f"Total cost: {round(weight, 2)}, profit: {round(profit, 2)}\n")


@time_exec
def main(file: str, max_invest) -> None:
    data = get_data(file)
    get_best_shares(data, max_invest)


if __name__ == "__main__":
    file, max_invest = user_selection()
    print(f"\n{'-'*50}")
    main(file, max_invest)
