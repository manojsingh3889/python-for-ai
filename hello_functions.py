#define function
def greet():
    print("hello function!!")
    print("hello again function!!")
    pass #readable way saying that this function return void -- optional

greet()


def check_weather(temp):
    if temp>25:
        print(f"its hot, temp is {temp}")
    else:
        print(f"its nice weather, temp is {temp}")
    pass

check_weather(30)
check_weather(25)


def greet_person(f_name="John", l_name="doe"): 
    print(f"Hello {f_name} {l_name}!!!")
    pass


greet_person("Manoj", "Singh")
greet_person("John")

greet_person(l_name="Singh")
greet_person(l_name="Singh", f_name="Manoj")


##retuirn function
def calculate_total(price, tax_rate, discount):
    return price * (1+tax_rate/100) - discount

my_total = calculate_total(price=100, tax_rate=30.5, discount=10)
print(my_total)


## return multiple value or packed return


def simple_function():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

first, last = simple_function()
print(first)
print(last)
print(first, last)