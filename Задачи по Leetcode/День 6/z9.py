# Задание 9


def maximumWealth(accounts):
    max_wealth = 0

    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth

    return max_wealth