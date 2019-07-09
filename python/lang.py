# monkey patching
class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def getName(self):
        return self.name

p = Person('Jian Li', 10)
print(p.getName())
def getName():
    return 'another name'
p.getName = getName
print(p.getName())

# generator

def generator():
    for i in range(10):
        yield i
print ('printing generator..')
for x in  generator():
    print(x)

def fibon(n):
    a ,b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
print 'print fibinache..'
for x in fibon(10):
    print x

# comphension dict
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
newmcase = {k+'_new': v+10 for k,v in mcase.items()}
print 'mcase: %s' % mcase
print 'newmcase: %s' % newmcase

# enumarate
for idx, value in enumerate([1,2,3,5,7,1,5],0):
    print idx, value


# global
foo = 'foo global'

def func():
    print 'foo before local assignment:'
    foo ='foo local'
    print 'foo after local assignment', foo

func()
print 'foo after the func call, i assume this is the global again:', foo

# shared global variables
import config

shared = config.declaredSharedVariable
print shared

from config import declaredSharedVariable
print 'using directly from import:',declaredSharedVariable

# python closures: allow the
def liner (a,b):
    def result(x):
        return a*x+b
    return result

a = liner(3, 4)
print a(3)

# example.log output
# C:\Users\Jian\PycharmProjects\interviewer\python>type example.log
# INFO:root:Running "add" with arguments (3, 3)
# INFO:root:Running "add" with arguments (4, 5)
# INFO:root:Running "sub" with arguments (10, 5)
# INFO:root:Running "sub" with arguments (20, 10)

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)
def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
        # Necessary for closure to work (returning WITHOUT parenthesis)
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

# metaclass exercises __init__, __new__, __call__

class Foo(object):

    def __init__(self,a,b ):
        print '__init__.. ', a, b

    def __call__(self, a, b):
        print '__call__ ...:',a, b

f = Foo('li', 'jian') # __init__ is called
f('jian', 'Li')  # __call__ is called

class counter:
    value = 0
    def set(self, x): self.value = x
    def up(self): self.value=self.value+1
    def down(self): self.value=self.value-1

count = counter()
count.set(5)
count.up()
count.down()
print 'after up and down, the value is:',count.value

print dir(count)