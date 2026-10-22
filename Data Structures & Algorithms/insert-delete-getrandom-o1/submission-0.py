class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.pos = {}
        

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        index = self.pos[val] #index of val in vals
        self.vals[index] = self.vals[-1]
        self.pos[self.vals[-1]] = index
        del self.vals[-1]
        self.pos.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()