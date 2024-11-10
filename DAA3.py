class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0

    for item in items:
        # If the entire item can be taken, add its full value
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fractional part of the item that fits
            total_value += item.ratio * capacity
            break

    return total_value

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
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in the knapsack is: {max_value}")
