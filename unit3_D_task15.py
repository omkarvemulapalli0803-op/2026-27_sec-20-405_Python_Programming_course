from functools import reduce

nums = [1, 2, 3, 4, 5]

print("Map:", list(map(lambda x: x*2, nums)))
print("Filter:", list(filter(lambda x: x%2 == 0, nums)))
print("Reduce:", reduce(lambda x, y: x+y, nums))