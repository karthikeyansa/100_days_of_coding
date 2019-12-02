class stack:
        def __init__(self):
                self.stack = []
        def push(self,element):
                self.stack.append(element)
        def pop(self):
                self.stack.pop()
        def print_stack(self):
                return self.stack
obj = stack()
while True:
        s = input('||push||pop||print||')
        if s == 'push':
                n = int(input('enter the element'))
                obj.push(n)
                print(obj.print_stack())
        elif s == 'pop':
                obj.pop()
                print(obj.print_stack())
        elif s == 'print':
                print(obj.print_stack())
        else:
                break
print('final:',print(obj.print_stack()))
