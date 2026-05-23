class MinStack:

    def __init__(self):
        self.stackd=[]
        self.minStack=[]


    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stackd.append(val)

    def pop(self) -> None:
        if self.stackd[-1]==self.minStack[-1]:
            self.minStack.pop()
        self.stackd.pop()

    def top(self) -> int:
        return self.stackd[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
