def minOperations(n):
    if n <= 1:
        return 0

    ops = 0
    clip = 0

    l = 1
    while l < n:
        # if l is a factor of n do copy and paste
        if n % l == 0:
            ops += 1
            clip = l  # copy
        # else just paste whats already in the clip
        l += clip  # paste
        ops += 1
        # count += 1

    return ops


n = 12
result = minOperations(n)
print(result)
