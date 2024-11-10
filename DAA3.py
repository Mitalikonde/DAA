# Write a program to solve a fractional Knapsack problem using a greedy method

class Weights:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.pw_ratio = profit / weight


def print_weights(arr):
    print("-----------")
    print(" W  P  P/W")
    for w in arr:
        print(w.weight, w.profit, round(w.pw_ratio, 2))
    print("-----------")


def cmp(item):
    return item.pw_ratio


def f_knapsack(arr, capacity):
    arr.sort(key=cmp, reverse=True)
    remaining_capacity = capacity
    total_profit = 0

    for w in arr:
        print("Selected -> Weight:", w.weight, "Profit:", w.profit, "P/W Ratio:", round(w.pw_ratio, 2))
        if w.weight <= remaining_capacity:
            remaining_capacity -= w.weight
            total_profit += w.profit
        else:
            total_profit += w.pw_ratio * remaining_capacity
            remaining_capacity = 0
            break
        print("Capacity Remaining:", remaining_capacity, "Profit:", total_profit)

    return total_profit


def main():
    n = int(input("Enter Number of Weights: "))
    arr = []

    for i in range(n):
        weight = int(input("Enter Weight " + str(i + 1) + ": "))
        profit = int(input("Enter Profit " + str(i + 1) + ": "))
        arr.append(Weights(weight, profit))

    print()
    print_weights(arr)

    capacity = int(input("Enter Capacity: "))
    print()

    max_profit = f_knapsack(arr, capacity)
    print("Maximum Profit:", max_profit)


if __name__ == "__main__":
    main()

 # Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.
def knapsack_01(weights, profits, n, m, dp):
    # Base case: no items left
    if n < 0:
        return 0

    # If already calculated, return the stored value
    if dp[n][m] != -1:
        return dp[n][m]

    # If the current item's weight exceeds the remaining capacity, skip it
    if weights[n] > m:
        dp[n][m] = knapsack_01(weights, profits, n - 1, m, dp)
    else:
        # Choose the maximum of either including or excluding the current item
        include = knapsack_01(weights, profits, n - 1, m - weights[n], dp) + profits[n]
        exclude = knapsack_01(weights, profits, n - 1, m, dp)
        dp[n][m] = max(include, exclude)

    return dp[n][m]

def main():
    weights = []
    profits = []

    # Input number of items and capacity of the sack
    n = int(input("Enter number of items: "))
    m = int(input("Enter capacity of sack: "))

    # Input the weights and profits of the items
    for i in range(n):
        weight = int(input("Enter weight " + str(i + 1) + ": "))
        profit = int(input("Enter profit " + str(i + 1) + ": "))
        weights.append(weight)
        profits.append(profit)

    # Initialize DP table with -1
    dp = [[-1 for _ in range(m + 1)] for _ in range(n)]

    # Get the maximum profit
    max_profit = knapsack_01(weights, profits, n - 1, m, dp)
    print("Maximum Profit:", max_profit)

if __name__ == "__main__":
    main()
