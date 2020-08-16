def hello(name=' kenneth'):
    print('THE HELLO() FUNCTION HAS BEEN CALLED')

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    if name != None:
        return greet

# x = hello()
# print(x()) 

def hi():
    return 'Hi Kenneth'

def other(func):
    return func()


print(other(hi))

# DEcorator

def deco(func):
    print('HEllO Kennmoh')

    def inner():
        print('Code here Before func() call')
        func()
        print('CAlled Func()')
    return inner

@deco
def need_deco():
    print('NEEDS DECORTOR')


# OR

# need_deco = deco(need_deco)
need_deco()


