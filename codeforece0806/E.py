import sys
import math
input = sys.stdin.readline

def min_operations_to_zero(l, r):
    total_sum = (r - l + 1) * (l + r) // 2
    # Counting the number of base-3 digits of the total_sum
    operations = 0
    while total_sum > 0:
        total_sum //= 3
        operations += 1
    return operations

t = int(input())
results = []

for _ in range(t):
    l, r = map(int, input().split())
    result = min_operations_to_zero(l, r)
    results.append(result)

for result in results:
    print(result)