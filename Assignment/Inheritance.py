# Inheritance
print("This is Inheritance: ")
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()
obj.display()

# Multiple Inheritance
print("This is Multiple Inheritance:")

class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def talent(self):
        print("Mother: Painting")

class Child(Father, Mother):
    def show(self):
        print("Child inherits both")

obj = Child()
obj.skills()
obj.talent()

# Multilevel Inheritance

print("This is Multiple Inheritance:")

class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

obj = Child()
obj.house()
obj.car()
obj.bike()

# Hierarchical Inheritance

print("This is Hierarchical Inheritance:")

class Parent:
    def property(self):
        print("Parent property")

class Child1(Parent):
    def show1(self):
        print("Child1 class")

class Child2(Parent):
    def show2(self):
        print("Child2 class")

obj1 = Child1()
obj2 = Child2()

obj1.property()
obj2.property()

# Hybrid Inheritance

print("This is Hybrid Inheritance:")

class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(A):
    def methodC(self):
        print("Class C")

class D(B, C):
    def methodD(self):
        print("Class D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()