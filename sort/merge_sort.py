def merge(lst, left, mid, right):
    i, j, k = left, mid + 1, left
    
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            k += 1
            i +=1
        else:
            tmp[k] = lst[j]
            k += 1
            j += 1
    
    if i > mid:
        for l in range(j, right+1):
            tmp[k] = lst[l]
            k += 1
    else:
        for l in range(i, mid+1):
            tmp[k] = lst[l]
            k += 1
    
    for l in range(left, right + 1):
        lst[l] = tmp[l]

def merge_sort(lst, left, right):
    if left< right:
        mid = (left + right) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)

lst = [5, 2, 3, 4, 1]
tmp = [0 for _ in range(len(lst) +1)]
merge_sort(lst, 0, len(lst) - 1)
print(lst)