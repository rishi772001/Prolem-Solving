'''
@Author: rishi
'''


# Implement Hashmap with collision using Linear probing
class Hashmap:
    def __init__(self):
        self.MAXSIZE = 5
        self.arr = [None for i in range(self.MAXSIZE)]

    def find_hash(self, key):
        if type(key) == int:
            return (2*key+1)%self.MAXSIZE
        elif type(key) == str:
            s = 0
            for i in range(len(key)):
                s += ord(key)
            return s%self.MAXSIZE
        else:
            raise TypeError("Only integers or strings are allowed")

    def __setitem__(self, key, value):
        h = self.find_hash(key)
        flag = True
        for i in range(self.MAXSIZE):
            temp = (h + i) % self.MAXSIZE
            if self.arr[temp] is None:
                self.arr[temp] = (key, value)
                flag = False
                break
        if flag:
            raise MemoryError("Memory limit exceeded")

    def __getitem__(self, key):
        h = self.find_hash(key)
        for i in range(self.MAXSIZE):
            temp = (h + i) % self.MAXSIZE
            if self.arr[temp] == None:
                continue
            if self.arr[temp][0] == key:
                return self.arr[temp][1]
        raise KeyError("Key does not exist")

    def __delitem__(self, key):
        h = self.find_hash(key)
        for i in range(self.MAXSIZE):
            if self.arr[i] == None:
                continue
            if self.arr[i][0] == key:
                self.arr[i] = None

    def __str__(self):
        return str(self.arr)

obj = Hashmap()
obj[1] = 10
obj[2] = 20
obj[3] = 30
obj["a"] = 1
del obj["a"]
print(obj['a'])
print(obj)