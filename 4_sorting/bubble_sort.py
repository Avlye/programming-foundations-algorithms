# Pros
# Very simple to understand and implement

# Cons
# Performance: O(n²)
# For loops insides of for loops are usually O(n²)


def bubbleSort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temporary_j = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temporary_j

        print("Current state: ", dataset)


bubbledList = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
bubbleSort(bubbledList)

print("Result: ", bubbledList)