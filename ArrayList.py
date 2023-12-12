class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self,pos):
        if 0<= pos < self.size:
            return self.array[pos]
        else:
            return None
        
    def insert(self, pos, e):
        if not self.isFull() and 0<=pos <= self.size :
         for i in range(self.size, pos, -1) :
            self.array[i] = self.array[i-1]
         self.array[pos] = e
         self.size += 1
        else: pass

    def delete(self,pos):
      if not self.isEmpty() and 0 <= pos < self.size :
        e = self.array[pos]
        for i in range(pos, self.size-1) :
            self.array[i] = self.array[i+1]
        self.size -= 1
        return e
      else: pass

    def __str__(self):
       return str(self.array[0:self.size])
    
    def replace(self, pos, e):
     if 0<=pos <= self.size :
      self.array[pos] = e

#연습문제 3.11 가장 큰 값 찾기 멤버 함수 구현
    def findMax(self):
     if self.isEmpty():
        return print('-1')    
     max = self.array[0]
     for i in range(1, self.size):
      if max < self.array[i] :
       max = self.array[i]
     print(max)
    
     #연습문제 3.12 가장 큰 값, 작은 값 찾기 멤버 함수 구현
    def findMinMax(self):
     if self.isEmpty():
        return print('(-1,-1)')    
     min = self.array[0]
     for i in range(1, self.size):
      if min > self.array[i]:
       min = self.array[i]
     
     max = self.array[0]
     for i in range(1, self.size):
       if max < self.array[i]:
        max = self.array[i]
     print(max,min)