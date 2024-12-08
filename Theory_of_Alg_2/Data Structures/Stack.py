class Stack:
    def __init__(self, max_n):
        self.arr = []
        self.max_n = max_n

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.max_n

    def push(self, value):
        if self.isFull():
            print("Stack is full")
            return
        self.arr.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.arr.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.arr[-1]

    def printStack(self):
        print(self.arr)


stack1 = Stack(10)
stack1.printStack()

stack1.push(5)
stack1.printStack()

stack1.push(10)
stack1.printStack()

print("Popped:", stack1.pop())
stack1.printStack()

print("Top element:", stack1.top())
