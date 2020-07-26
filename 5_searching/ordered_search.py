# Time complexity: O(n log n)

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist):
    listsize = len(itemlist) - 1

    lowerIndex = 0
    upperIndex = listsize

    while lowerIndex <= upperIndex:
        mid = (lowerIndex + upperIndex) // 2

        if itemlist[mid] == item:
            return mid

        if item > itemlist[mid]:
            lowerIndex = mid + 1
        else:
            upperIndex = mid - 1

    if lowerIndex > upperIndex:
        return None


print(binarysearch(12, items))  # Should be None
print(binarysearch(49, items))  # Should be 6
