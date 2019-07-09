# question One
# print out 1 t0 100 on the condition if input is mutiplier of 3 'Fizz' if 5 'Buzz' if both 3 and 5 print 'FizzBuzz'
['FizzBuzz' if x % 2 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 ==0 else x for x in range (1,101)]

# question two
# print out the numbers between dups [5,4,1,2,3,4,5]->41234 123
l = [5, 4, 1, 2, 3, 4, 5]
lc = [x for x in l if l.count(x) == 2]
lcs = set(lc)
print 'dups',lcs

for x in lcs:
    for i in range(len(l)):
        k = 0
        if l[i] == x:
            k = i + 1
            while l[k] != x:
                print l[k]
                k += 1
            print 'next'
            break



