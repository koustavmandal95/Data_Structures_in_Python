def linearsearch(arr,key):
    flag=0
    position=0
    for i in arr:
        if key==i:
            return ("found key at %d %d" % (key,position))
            flag=flag+1
        position=position+1
    if flag==0:
        print("The key %d not found" % (key))
if __name__=="__main__":
    key=int(input("enter the key to search"))
    arr=list(map(int,input("Enter the string").rstrip().split()))
    print(linearsearch(arr,key))
    
    