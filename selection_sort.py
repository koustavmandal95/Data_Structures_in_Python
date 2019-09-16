def selection_sort(arr):
    iterations=0
    for i in range(len(arr)-1):
        index=i
        for j in range(i+1,len(arr)):
            iterations=iterations+1
            if arr[j]<arr[index]: # Find the smallest element in sub_array (i+1-nth)
                index=j
        if index!=i:# Only do when index are different . # save one write operations
            arr[i],arr[index]=arr[index],arr[i]
    print("the Number of iterations",iterations) # (n*(n-1)/2) n=5
    return arr
if __name__=="__main__":
    arr=list(map(int,input("Enter the element ").rstrip().split()))
    result=selection_sort(arr)
    print(result)
