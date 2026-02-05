class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxcount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_count = 1 + self.count.get(val,0)
        self.count[val] = val_count
        if val_count > self.maxcount:
            self.maxcount = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxcount].pop()
        self.count[res] -= 1
        if not self.stacks[self.maxcount]:
            self.maxcount -= 1
        return res 
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()