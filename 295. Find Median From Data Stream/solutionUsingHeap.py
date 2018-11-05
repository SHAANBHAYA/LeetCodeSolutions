import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap=[]
        self.minHeap=[]
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def rebalanceHeap(self):
        if len(self.maxHeap)-len(self.minHeap)>=2:
            num=heapq.heappop(self.maxHeap)*-1
            heapq.heappush(self.minHeap,num)
        else:
            num = heapq.heappop(self.minHeap)*-1
            heapq.heappush(self.maxHeap, num)


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if(len(self.minHeap)==0 or num>self.minHeap[0]):
            heapq.heappush(self.minHeap,num)
        else:
            num=num*-1
            heapq.heappush(self.maxHeap,num)

        if abs(len(self.maxHeap)-len(self.minHeap))>=2:
            self.rebalanceHeap();






    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap)==len(self.maxHeap):
            return float(((self.maxHeap[0]*-1)+self.minHeap[0])/2)
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0]*-1


a=MedianFinder()
a.addNum(-1)
med=a.findMedian()
a.addNum(-2)
med=a.findMedian()
a.addNum(-3)
med=a.findMedian()
a.addNum(-4)
med=a.findMedian()
a.addNum(-5)
