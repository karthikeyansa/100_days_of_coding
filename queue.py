class Queue:
    def __init__(self):
        self.queue = []

    def push(self,value):
        self.queue.append(value)
        self.display_queue()

    def pop(self):
        self.queue.pop()
        self.display_queue()

    def display_queue(self):
        print(self.queue)
queue = Queue()
try:
    while(True):
        action = input("push or pop")
        if action == "push" :
            n = int(input('enter the number'))
            queue.push(n)
        elif action == "pop" :
            queue.pop()
        else:
            break
except Exception as e:
    print(str(e))
    
    
