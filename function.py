thislist = ["apple", "banana", "cherry"]
print(len(thislist))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)
newnewlist =[ x for x in fruits if x != "apple"]
print(newnewlist)


def my_function():
    print(True)
    
my_function()

temp1 = 77
celscius1 = (temp1 - 32) * 5/9
print(celscius1)

def get_string():
    return "try"

message = get_string()
print(message)

def mymy_func():
    pass


#fuction arguments

def func_arg(fname, mname):
    print(fname + mname + " Refsnes")
    
func_arg("emil", " m")
func_arg("ronel", " v")
func_arg("linus", " a")


def my_funfunc(fruits):
    for fruit in fruits:
        print(fruit)
    
my_fruits = ["apple", "banana", "cherry"]
my_funfunc(my_fruits)


def position_only(name, /):
    print("Hello", name)
    
position_only("emil")

def keyWord(*, name):
    print("Hello", name)
    
keyWord(name = "Emil")

def combinekeyPosition(a, b, /, *, c, d):
    return a + b + c + d
    
result = combinekeyPosition(5, 10, c = 15, d=20)
print(result)

def myargs(*kids):
    print("the youngest child is " +kids[2])
    
myargs("emil", "Tobias", "linus")


def mykwargs(**kids):
    print("his last name is " + kids["lname"])
    
mykwargs(fname = "tobias", lname = "refsnes")


def bothArgs(title, *args, **kwargs):
    print("title:", title)
    print("positional argument:", args)
    print("keyword argument:", kwargs)
    
bothArgs("user info", "Emil", "Tobias", age = 25, city = "oslo")

def unfuck(a, b, c):
    return a + b + c
    
numbers = [1, 2, 3]
result = unfuck(*numbers)
print(result)










