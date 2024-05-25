class Solution:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        for i in range(n-1,0,-1):
            count = 0
            if count != 0:
                break
            else:
                for j in range(0,i):
                    if arr[j]>arr[j+1]:
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
                    else:
                        count = count+1
        
        