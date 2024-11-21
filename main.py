# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']
print(drawers[1])
drawers[2] = "useless manuals"
print(drawers)
# What should the list look like now?
# Print the list! Does it match your prediction?


my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3


some_nums = [44, 56, 2, 3, 12, 19, 6]
print("Get started by writing your own code!")
# Some optional challenges to assess and refine your understanding:
print(len(some_nums))
# Use antoher python built-in function and print the result.
some_nums.pop()
print(some_nums)
# Utilize a method from the documentation and print the result.


for count in range(0, 5):
    print("looping =", count)

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1


def say_hi(name):
    print("hi, " + name)


say_hi('itachi')


def say_hi(name):
    return "Hi " + name


greeting = say_hi("Michael")  # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting)  # this will output 'Hi Michael'


def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print(sum1)
print(sum2)
print(sum3)


# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)


be_cheerful()  # output: good morning (repeated on 2 lines)
be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")  # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)  # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)  # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")  # output: good morning kb (repeated on 3 lines)


def multiply(num_list, num):
    for x in num_list:
        x += num
    return num_list


a = [2, 4, 10, 20]
b = multiply(a, 5)
print(b)
