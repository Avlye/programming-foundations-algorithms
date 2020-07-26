# Pros
# key-to-value mapping are unique
# hash tables are typically very fast

# Cons
# For small datasets, arrays are usually more efficient
# Hash tables don't order entries in a predictable way

# Create a hashtable all at once
items = {"key1": 1, "key2": 2, "key3": 3}
print(items)

items['random key'] = 'random value'
print(items)

for key, value in items.items():
    print(key, value)
