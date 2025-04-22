def calculateprofit(arr,arrsize):
    profit=0
    for i in range(1,arrsize):
        if arr[i]>arr[i-1]:
            profit=arr[i]-arr[i-1]
    return profit
arr=[234,543,124,890,157,908,376]
arrsize=len(arr)
print("Max profit is ",calculateprofit(arr,arrsize))

