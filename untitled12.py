import time
start=time.time()
class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
         return self.items ==[]
    def push(self,item):
        self.items.append(item)
        print(item)
    def pop (self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def seze(self):
        return len(self.items)
s=stack()
print(s.isempty())
print("push operation")
s.push(11)
s.push(12)
s.push(13)
time.sleep(2)
print("the topmost element is", s.peek ())
print("pop operation")
print("The deleted element is",s.pop ())
print("The deleted element is",s.pop ())
end=time.time()
print(f"runtime of the program is {end-start}") 

