from collections import deque

# Create a new empty deque
queue = deque()

# Add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Print the queue contents
print(queue)
print(queue[0])

# Remove first item from queue
item_popped = queue.popleft()

print(queue)
print(item_popped)
