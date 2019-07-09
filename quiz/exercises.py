# find the max in a liat
def findmax(l):
    max = 0
    for x in range(len(l)):
        if l[x]>=max:
            max=l[x]
    print max

l = [5, 4, 7, 3, 32, 5]
findmax(l)


# reverse sting use stack
str='abcd'
stack=[]
for x in str:
    stack.append(x)

for x in range(len(str)):
    print stack.pop()