for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))
#--------------------------------------------------
for i in range(4):
    print(i)

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)
#--------------------------------------------------
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement
add(5,6)
#--------------------------------------------------
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""


args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            
all_the_args(**kwargs)        
all_the_args(*args, **kwargs)  
#---------------------------------------------------------
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num    # => 43
    print(x)   # => 43

def set_global_x(num):
    global x
    print(x)   # => 5
    x = num    # global var x is now set to 6
    print(x)   # => 6

set_x(43)
set_global_x(6)

#-------------------------------------------------

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3) 
