# Divide and conquer algorithm
# Performs better than merge sort
# Worst case is O(n2) when data is mostly sorted already

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def quicksort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivot = partition(dataset, first, last)

        # now sort the two partitions
        quicksort(dataset, first, pivot)
        quicksort(dataset, pivot + 1, last)


def partition(dataset, first, last):
    # choose the first item as the pivot
    pivotvalue = dataset[first]
    # establish the upper and lower index
    lower = first + 1
    upper = last

    # Start seaching for the crossing paths
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and dataset[lower] <= pivotvalue:
            lower += 1

        # advance the upper index
        while upper >= lower and dataset[upper] >= pivotvalue:
            upper -= 1

        # if the two indexes cross, we found the split point
        if upper < lower:
            done = True
        else:
            temporary_lower = dataset[lower]
            dataset[lower] = dataset[upper]
            dataset[upper] = temporary_lower

    # when the split point is found, exchange the pivot value
    temporary_first = dataset[first]
    dataset[first] = dataset[upper]
    dataset[upper] = temporary_first

    # return the split point index
    return upper


print(items)
quicksort(items, 0, len(items) - 1)
print(items)