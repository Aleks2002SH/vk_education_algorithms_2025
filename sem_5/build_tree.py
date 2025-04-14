class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.data = val
        self.left = left
        self.right = right
        self.balanceFactor = 0

def buildTree(arr,i):
    if i>=len(arr) or arr[i]==None:
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr,2*i+1)
    root.right = buildTree(arr,2*i+2)
    return root

def depthTraversal(root,res):
    if root == None:
        return res
    depthTraversal(root.left,res)
    res.append(root.data)
    depthTraversal(root.right,res)
    return res


class MaxHeap:
    def __init__(self,data):
        n = len(data)
        self.data = data
        for i in range(n/2-1,0,-1):
            self.siftDown(n,i)
    
    def siftDown(self,n,i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and self.data[left]>self.data[largest]:
            largest = left
        if right<n and self.data[right]>self.data[largest]:
            largest = right
        if largest != i:
            self.data[i],self.data[largest] = self.data[largest],self.data[i]
            self.siftDown(n,largest)
    
    def top(self):
        return self.data[0]
    
    def right(self,i):
        return 2*i+2
    
    def left(self,i):
        return 2*i+1
    
    def parent(self,i):
        if i == 0:
            return i
        return (i-1)//2
    
    def push(self,elem):
        self.data.append(elem)
        self.up(self,len(self.data)-1)

    def up(self,ind):
        while self.data[ind]>self.data(self.parent(ind)):
            self.data[ind],self.data[self.parent(ind)] = self.data[self.parent(ind)],self.data[ind]
            ind = self.parent(ind)
        
    
    def deleteMax(self):
        if (len(self.data)==0):
            return None
        n = len(self.data)
        res = self.data[0]
        self.data[0] = self.data[n-1]
        self.data.pop()
        self.siftDown(n-1,0)
        return res
    
class MinHeap:
    def __init__(self,data):
        n = len(data)
        self.data = data
        for i in range(n/2-1,0,-1):
            self.siftDown(n,i)
    
    def siftDown(self,n,i):
        smallest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and self.data[left]<self.data[smallest]:
            smallest = left
        if right<n and self.data[right]<self.data[smallest]:
            smallest = right
        if smallest != i:
            self.data[i],self.data[smallest] = self.data[smallest],self.data[i]
            self.siftDown(n,smallest)
    
    def top(self):
        return self.data[0]
    
    def right(self,i):
        return 2*i+2
    
    def left(self,i):
        return 2*i+1
    
    def parent(self,i):
        if i == 0:
            return i
        return (i-1)//2
    
    def push(self,elem):
        self.data.append(elem)
        self.up(self,len(self.data)-1)

    def up(self,ind):
        while self.data[ind]<self.data(self.parent(ind)):
            self.data[ind],self.data[self.parent(ind)] = self.data[self.parent(ind)],self.data[ind]
            ind = self.parent(ind)
        
    
    def deleteMin(self):
        if (len(self.data)==0):
            return None
        n = len(self.data)
        res = self.data[0]
        self.data[0] = self.data[n-1]
        self.data.pop()
        self.siftDown(n-1,0)
        return res
    
class MinHeap_ksorted:
    def __init__(self):
        self.data = []

    def heappush(self, value, array_idx, element_idx):
        self.data.append((value, array_idx, element_idx))
        self._heapify_up(len(self.data) - 1)

    def heappop(self):
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._heapify_down(0)
        return root

    def _heapify_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx][0] < self.data[parent][0]:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _heapify_down(self, idx):
        n = len(self.data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right

            if smallest == idx:
                break
            self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
            idx = smallest

    def is_empty(self):
        return len(self.data) == 0
