def left_rotate(a,d):
    loop=d
    arr=a
    for i in range(len(arr)):
        temp=arr[0]
        if loop>0:
            for j in range(0,len(arr)-1):
                arr[j]=arr[j+1]
            arr[-1]=temp
        loop=loop-1
    print(arr)


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result=left_rotate(a,d)
