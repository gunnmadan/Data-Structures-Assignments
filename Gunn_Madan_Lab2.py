def arr_resize(arr, capacity, isUpsizing):
    #Determine the new capacity based on isUpsizing
    if isUpsizing: 
        new_capacity = int(capacity * 1.25)
    else: 
        new_capacity = int(capacity * 0.75)
#Initialize the new array with None
    new_arr = [None] * new_capacity
#Copy the elements from arr to new_arr
    for i in range (min(len(arr), new_capacity)):
        new_arr[i] = arr[i]

    print(new_arr)
    return new_arr

#Test cases
arr_resize([1,2,3,4,5,6,7,8], 8, True) 
arr_resize([1,2,3,4], 4, True)
arr_resize([1,2,3, None, None, None, None, None], 8, False)
arr_resize([1,2,3, None, None, None], 6, False) 