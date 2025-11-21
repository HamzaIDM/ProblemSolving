import sys

def binarySearch(arr,low,high,x):
    bingo = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            bingo = mid+1
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
    return bingo

def main():
    read = sys.stdin.readline
    write = sys.stdout.write

    n = int(read())
    l = list(map(int,read().split()))

    q = int(read())
    m = list(map(int,read().split()))
    l.sort()
    for i in m:
        print(binarySearch(l,0,len(l)-1,i))

if __name__ == '__main__':
    main()
