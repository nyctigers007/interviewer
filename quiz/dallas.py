# question one
# write a decorator

def decorator(func_var):
    def wrapper(*args, **kwargs):
        print ('wrap begin...')
        func_var(*args, **kwargs)
        print ('wrap end...')

    return wrapper

@decorator
def say_hello(words):
    print 'hello', words

say_hello('world!')

print '******'*3
def say_whee():
    print 'whee'
say_whee = decorator(say_whee)
print say_whee()
print say_whee # <function wrapper at 0x02422B30>

# question two
# function parameters

def func1(*args, **kwargs):
    for x in args:
        print x
    for k, v in kwargs.items():
        print 'key:{}:value:{}'.format(k, v)

func1("jian","li","wang", "zhe", name='jian', age='twentysix')

# question three
# class in python

class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name:{}; age:{}'.formate(self.name, self.age)

    def getName(self):
        return  self.name

p = person('jian Li', 93)
print p.name, p.age

# monkey patch
def getAnotherName():
    return 'another name'
p.getName = getAnotherName
print(p.getName())

# question four
# open r w r+ a
f = open('file.txt', 'w')
f.write('this is a test line\n')
f.write('this is another test line')
f.flush()
f.close()
fr = open('file.txt','r')
for x in fr.readlines():
    print(x)
fr.close()

with (open('file.txt', 'r')) as f:
    for x in f.readlines():
        print (x)

# question five
# open a mysql db connection
# conn = open(dbhost='localhost', dbname='mydb', usernm='admin', passwd='admin')
# cursor = conn.cursor()
# cursor.execute('select * from test;')
# for x in cursor.fetchall():
#     print (x)
# cursor.close()
# conn.close()