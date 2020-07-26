# BigO(n) time complexity

items = ["apple", "pear", "orange", "apple", "pear"]

counter = {}

for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)