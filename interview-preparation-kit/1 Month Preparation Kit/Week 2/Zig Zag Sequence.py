def findZigZagSequence(a, n):
    a.sort()
    mid = int(n//2) # fix how to find the mid index of array with odd elements
    a[mid], a[n-1] = a[n-1], a[mid]

    
    # mid and last element already swapped
    # so another swap needed start from the 
    # second last element and next element from mid
    st = mid + 1
    ed = n - 2 
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        # add value of st and 
        # substract value of ed
        st = st + 1
        ed = ed - 1 

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
