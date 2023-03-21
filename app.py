class Queue:
    def __init__(self,sizeOfQueue):
        self.l1=[]
        self.sizeOfQueue= sizeOfQueue
        
    def enqueue(self,val):
        if len(self.l1)<self.sizeOfQueue:
         self.l1.append(val)
    def showqueue(self):
        return self.l1
    def deque(self):
        self.l1.pop(0)
    def peak(self):
        return self.l1[-1]
    def isFull(self):
        if len(self.l1)==self.sizeOfQueue:
            print("Queue is full")
        else:
            print("Queue is not full")
    def isEmpty(self):
        if len(self.l1)==0:
            print("queue is empty")
        else:
            print("queue is not empty")  
                              
obj=Queue(5)
obj.enqueue(1)
print(obj.showqueue()) 
obj.enqueue(2)
print(obj.showqueue()) 
obj.enqueue(3)
print(obj.showqueue()) 
obj.enqueue(4)
print(obj.showqueue()) 
obj.enqueue(5)
print(obj.showqueue()) 
obj.showqueue()
obj.deque()
print(obj.showqueue())  
print(obj.peak())              