class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapsack_0_1(capacity, items):
    n = len(items)
    # Create a DP table where dp[i][w] is the max value for the first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight <= w:
                # Include the item or exclude it, take the maximum
                dp[i][w] = max(items[i - 1].value + dp[i - 1][w - items[i - 1].weight], dp[i - 1][w])
            else:
                # Cannot include the item, take the value without it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Input number of items
n = int(input("Enter the number of items: "))
items = []

# Input item details
for i in range(n):
    value = int(input(f"Enter value for item {i + 1}: "))
    weight = int(input(f"Enter weight for item {i + 1}: "))
    items.append(Item(value, weight))

# Input knapsack capacity
capacity = int(input("Enter the capacity of the knapsack: "))

# Calculate the maximum value for the given knapsack capacity
max_value = knapsack_0_1(capacity, items)
print(f"Maximum value in the knapsack is: {max_value}")
