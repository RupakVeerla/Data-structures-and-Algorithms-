#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.array.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.array:
          return self.array.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.array:
          return self.array[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.array:
          return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
