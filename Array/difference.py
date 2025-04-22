def difference(arr,arrsize):
    profit=0
    for i in range(1,arrsize):
        if arr[i]>arr[i-1]:
            diff=arr[i]-arr[i-1]
    return diff
arr=[234,543,124,890,157,908,376]
arrsize=len(arr)
print("difference is ",difference(arr,arrsize))