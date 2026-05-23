class MinStack:

    def __init__(self):
        self.stackd=[]

    def push(self, val: int) -> None:

        self.stackd.append(val)

    def pop(self) -> None:
        self.stackd.pop()

    def top(self) -> int:
        if len(self.stackd)<0:
            return -1
        else:
            return self.stackd[-1]

    def getMin(self) -> int:
        num=sorted(self.stackd)
        return num[0]
