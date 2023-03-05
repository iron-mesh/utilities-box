
class Proto:
    field = []


class Child1(Proto):
    @classmethod
    def func(cls):
        cls.field.append(1)

class Child2(Proto):
    @classmethod
    def func(cls):
        cls.field.append(2)


(Child1.func())
(Child2.func())
print(Proto.field)
print(Child1.field is Proto.field)