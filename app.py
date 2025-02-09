import tkinter as tk
from tkinter import Scrollbar

# Text content for Homework1
homework1_text = """# abs()
print(abs(-20))
# all()
print(all(['h', 'b', 'y']))
# any()
print(any(['no', 0, ()]))
# ascii()
print(ascii('mesut özil'))
# bool()
print(bool(1))
# bin()
print(bin(15))
# bytearray()
print(bytearray([2, 3, 5, 7]))
# bytes()
print(bytes('Ali is my friend', 'utf-8'))
# callable()
x = 5
print(callable(x))

def testFunction():
    print("Test")

y = testFunction
print(callable(y))
# chr()
print(chr(97))
# classmethod()
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

Person.printAge = classmethod(Person.printAge)
Person.printAge()
# compile()
codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')
exec(codeObject)
# complex()
print(complex(2, -3))
# delattr()
class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate() 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
delattr(Coordinate, 'z')
print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)
## Raises Error
#print('z = ',point1.z)

# dict()
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))
empty = dict()
print('empty =', empty)
print(type(empty))

# dir()
number = [12]
print(dir(number))

# enumerate()
languages = ['Python', 'Java', 'JavaScript']
print(list(enumerate(languages)))
# eval()
number = 9
square_number = eval('number * number')
print(square_number)
# exec()
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)
# filter()
def check_even(number):
    if number % 2 == 0:
        return True  
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_iterator = filter(check_even, numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers)
# float()
print(float('34'))
# format()
value = 45
binary_value = format(value, 'b')
print(binary_value)
# frozenset()
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())
# getattr()
class Student:
    marks = 88
    name = 'Sheeran'

person = Student()
name = getattr(person, 'name')
print(name)
marks = getattr(person, 'marks')
print(marks)
# globals()
print(globals())
# hasattr()
class Person:
    age = 23
    name = "Adam"

person = Person()
print("Person's age:", hasattr(person, "age"))
print("Person's salary:", hasattr(person, "salary"))
# hash()
text = 'Python Programming'
hash_value = hash(text)
print(hash_value)
# hex()
number = 435
print(number, 'in hex =', hex(number))
# help()
print(help(enumerate))
# id()
a = 15
print(id(a))
# input()
x = input('Are you ok?')
#  int()
n = '11'
print(int(n))
# isinstance()
numbers = [1, 2, 3, 4, 2, 5]
result = isinstance(numbers, list)
print(result)
# issubclass()
class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')
print(issubclass(Triangle, Polygon))
# iter()
phones = ['iphone', 'samsung', 'xiaomi']
print(next(iter(phones)))
# len()
print(len('hello world'))
# list()
#print(list(1,2,3,4))
# locals()
print(locals())
# map() Function
numbers = [1,2,3,4]
def square(number):
    return number * number

squared_numbers = map(square, numbers)
result = list(squared_numbers)
print(result)
# max()
max_no = max(15,16,17)
print(max_no)
# memoryview()
#random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
mv = memoryview(random_byte_array)
print(mv[0])
print(bytes(mv[0:2]))
print(list(mv[0:3]))
# min()
min_no = min(15,16,17)
print(min_no)
# next()
phones = ['iphone', 'samsung', 'xiaomi']
print(next(iter(phones)))
print(next(iter(phones)))
print(next(iter(phones)))
# object()
test = object()
print(type(test))
#  oct()
print(oct(13))
# open()
#f = open('neuro.txt', 'r')
#  ord()
print(ord('F'))
#  pow()
print(pow(2, 3))
# print()
print('Hello world')
#  property()
class Person:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        print('Getting name')
        return self._name
    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value
    def del_name(self):
        print('Deleting name')
        del self._name
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name
#  range() Function
for i in range(5):
    print('I Love YOU?')
# repr()
numbers = [1, 2, 3, 4, 5]
printable_numbers = repr(numbers)
print(printable_numbers)
# reversed()
print(reversed('Python'))
# round()
n1 = 35.66667
print(round(n1))

# set()
n2 = 'hello'
print(set(n2))

# setattr()
class Person:
    name = "John"
    age = 36
    country = "Norway"

setattr(Person, 'age', 40)

# slice()
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

# sorted()
a = (1, 11, 2)
x = sorted(a)
print(x)

# staticmethod()
class Calculator:

    def total(num1, num2):
        return num1 + num2
Calculator.total = staticmethod(Calculator.total)
sum = Calculator.total(5, 7)
print('Sum:', sum)
# str()
n3 = 16
print(str(n3))
# sum()
# numbers = [2.5, 3, 4, -5]
# numbers_sum = sum(numbers)
# print(numbers_sum)
# super()
class Parent:
    def __init__(self, txt):
        self.message = txt
    def printmessage(self):
        print(self.message)
class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)
x = Child("Hello, and welcome!")
x.printmessage()
# tuple()
t = tuple([1,5,6,7])
print(t)
# type()
n6 = 'Abas'
print(type(n6))
# vars()
print(vars(int))
# zip()
languages = ['Reza', 'Anwar', 'Anahita']
versions = [14, 13, 16]
result = zip(languages, versions)
print(list(result))
# __import__()
np = __import__('numpy', globals(), locals(), [], 0)
a = np.array([1, 2, 3])
print(type(a))
"""

homework2_text = """def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 7
for i in range(n):
    print(fibonacci(i))
"""

homework3_text = """def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)


num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')
"""

# Create the main Tkinter window
root = tk.Tk()
root.title("Homework Text App")

# Create a menu bar
menubar = tk.Menu(root)

# Create Homework menus
homework1_menu = tk.Menu(menubar, tearoff=0)
homework1_menu.add_command(label="View Homework", command=lambda: text_area.delete(1.0, tk.END) or text_area.insert(tk.END, homework1_text))

homework2_menu = tk.Menu(menubar, tearoff=0)
homework2_menu.add_command(label="View Homework", command=lambda: text_area.delete(1.0, tk.END) or text_area.insert(tk.END, homework2_text))

homework3_menu = tk.Menu(menubar, tearoff=0)
homework3_menu.add_command(label="View Homework", command=lambda: text_area.delete(1.0, tk.END) or text_area.insert(tk.END, homework3_text))

# Add Homework menus to the menu bar
menubar.add_cascade(label="Python built-in functions", menu=homework1_menu)
menubar.add_cascade(label="Fibonnaci series", menu=homework2_menu)
menubar.add_cascade(label="Tower of Hanoi", menu=homework3_menu)

# Configure the root window to use the menu bar
root.config(menu=menubar)

# Create a vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a text area
text_area = tk.Text(root, wrap=tk.WORD, width=80, height=20, yscrollcommand=scrollbar.set)
text_area.pack(padx=10, pady=10)

# Configure the scrollbar to work with the text area
scrollbar.config(command=text_area.yview)

# Start the Tkinter main loop
root.mainloop()
