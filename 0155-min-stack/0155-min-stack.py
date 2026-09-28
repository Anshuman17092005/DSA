class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            if value <= self.minStack[-1]:
                self.minStack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()