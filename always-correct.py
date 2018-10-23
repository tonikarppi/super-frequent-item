from math import floor


# Finds the item that appears at least 90% of the time in the input list,
# or None if no such item exists.
# This algorithm is always correct, and has complexity O(n*log(n)).
def find_super_frequent_item(A):
    n = len(A)
    A = sorted(A)
    x = A[floor(n/2)]
    count = 0

    for i in range(0, n):
        if A[i] == x:
            count = count + 1

    if count >= 0.9 * n:
        return x

    return None


A1 = [1, 1, 1, 1, 1, 5, 1, 1, 1, 1]
A2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
A3 = [1, 1, 4, 1, 1, 1, 3, 1, 1, 1]

result1 = find_super_frequent_item(A1)
result2 = find_super_frequent_item(A2)
result3 = find_super_frequent_item(A3)

print(result1)
print(result2)
print(result3)
