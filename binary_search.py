def binary_search(input_array, value):
    """Your code goes here."""
    len_=len(input_array)
    input_array.sort(reverse=False)
    mid=len_//2
    if input_array[mid]>=value:
        for i in range(0,mid):
            if input_array[i]==value:
                return(i)
            else:
                return -1
    elif input_array[mid]<value:
        for i in range(mid+1,len_):
            if input_array[i]==value:
                return(i)
            else:
                return -1
            

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
