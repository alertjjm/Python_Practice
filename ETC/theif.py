def kth(a,k):
    less, big = [], []
    pivot = a[0]
    for i in a[1:]:
        if i <= pivot:
            less.append(i)
        else:
            big.append(i)
    if len(less) >= k:
        return kth(less, k)
    elif len(less)+1==k:
        return pivot
    else:
        return kth(big, k-len(less)-1)
sample=[6,4,8,7,9,5,1,1,5,2,4,1]
print(kth(sample,4))