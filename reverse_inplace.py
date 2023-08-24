def reverse_inplace(arr):
    temp = list(arr)
    for i in range(1, len(arr) + 1):
        print(temp[-i])
        arr[i-1] = temp[-i]

    return arr


my_list = [1, 2, 3, 4, 5]

reverse_inplace(my_list)

print(my_list)

print(my_list[:-1])
