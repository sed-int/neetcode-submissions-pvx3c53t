class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.minSt.append(min(val, self.minSt[-1] if self.minSt else val))

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
