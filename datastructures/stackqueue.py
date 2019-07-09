class stack(object):
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
    def pop (self):
        if len(self.stack):
            return self.stack.pop()
    def poptop(self):
        if (len(self.stack)):
            return self.stack.pop(0)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

for x in range(4):
    print s.pop()

print 'queue and dequeue'
q = stack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)

for x in range(4):
    print q.poptop()
