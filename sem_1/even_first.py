class Solution(object):
    
    def even_first(self,arr):
        evenind = 0
        for i in range(len(arr)):
            if (arr[i]%2 ==0):
                arr[i],arr[evenind] = arr[evenind],arr[i]
                evenind+=1
        return arr