# reverse list
l=[1,2,4,5,6,7,9]
print 'using index operator to reverse:',l[::-1]
rev = list()
for x in range(len(l)-1, 0-1, -1):
    rev.append(l[x])
print 'using loop to reverse::', rev

# using a stack
rev = []
for x in range(len(l)):
    rev.append(l.pop())
print 'using stack pop:',rev

# use reversed and list comprehension
l=[1,2,4,5,6,7,9]
lr = list(x for x in reversed(l))
print 'using reversed:', lr

# remove duplicates O(n)
l=[1,2,4,5,6,7,9,2,5]
newlist = []
for i in range(len(l)):
    if l[i] not in newlist:
        newlist.append(l[i])
    else:
        print 'duplicate:%s' % l[i]
print 'remove dup with loop', newlist

lu = set(l)
print 'remove duplicates with set:', lu

# lambda method
f = lambda x: x*x
li = [f(x) for x in range(10)]
print 'using lambda in list', li

li = [i*2 for i in range(10)]
print 'using list comprehesion', li

li = [map(lambda x: x*2, range(10))]
print 'using map', li

li = [filter(lambda x: x % 2 == 0, range(10))]
print 'using filtering:', li

li = [x for x in range(10) if x % 2 == 0]
print 'using list comprehension for filtering:', li

# sort one list by another list
list1 = ["what", "I'm", "sorting", "by"]
list2 = ["something", "else", "to", "sort"]
pairs = zip(list1, list2)
pairs.sort()
results = [x[1] for x in pairs]
print 'after sorting:', results

# question:
# find the numbers that multiple = 20
l = [1, 4, 3, 6, 8, 9, 5]
# 1) brute force O(N*N)
for x in l:
    for z in l:
        if x*z ==20:
            print 'found %d * %d = %d' % (x,z,x*z)

# 2) scan + look up O(N)
for x in l:
    z = 20/x
    if z in l and z * x == 20:
        print '%d * %d = %d' % (z, x, z*x)

# QUESTION
# combime 2 lists into one and sorted
l1= [3, 2, 5]
l2 = [1,4,8]

