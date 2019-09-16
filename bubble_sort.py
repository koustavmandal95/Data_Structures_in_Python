def bubble_sort(arr):
    iterations=0
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-i-1):   # It decreases with every i  
            iterations=iterations+1     # with every iteration of i = largst element goes end of sorted array 
            if arr[j]>arr[j+1]: # Asc or desc depends on >,< sign
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("the Number of iterations",iterations) # (n*(n-1)/2) n=5
    return arr
if __name__=="__main__":
    arr=list(map(int,input("Enter the element ").rstrip().split()))
    result=bubble_sort(arr)
    print(result)
