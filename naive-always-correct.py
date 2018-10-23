

# Finds the item that appears at least 90% of the time in the input list,
# or None if no such item exists.
# This algorithm is always correct, and has complexity O(n^2).
def find_super_frequent_item(A):
    n = len(A)
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if A[i] == A[j]:
                count = count + 1
        if count >= 0.9 * n:
            return A[i]

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
