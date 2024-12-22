def add(datatype, *args):
    answer = 0 if datatype == 'int' else ''
    for x in args:
        answer += x
    print(answer)

add('int', 5, 6)
add('str', 'Hi ', 'Geeks')


def add(a=None, b=None):
    print(a if b is None else a + b)

add(2, 3)
add(2)

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    print(first * second)

@dispatch(int, int, int)
def product(first, second, third):
    print(first * second * third)

@dispatch(float, float, float)
def product(first, second, third):
    print(first * second * third)

product(2, 3)
product(2, 3, 2)
product(2.2, 3.4, 2.3)