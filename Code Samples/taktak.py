

class Grandpa:
    pass

class Mixer:
    pass

class Father(Grandpa):
    pass

class Son(Father, Mixer):
    pass



def print_bases(cls):
    if cls.__bases__:
        print(f"Class {cls.__name__} has bases: {cls.__bases__}")
        for i in cls.__bases__:
            print_bases(i)

def check():
    raise Exception("Ti che durak")
    print("Hello")



print(issubclass(Mixer, Grandpa))
check()