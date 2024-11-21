def Countdown(number):
    return list(range(number, -1, -1))


print(Countdown(10))


def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]


result = print_and_return([1, 2])
print(result)


def first_plus_length(lst):
    return lst[0] + len(lst)


result_3 = first_plus_length([1, 2, 3, 4, 5])
print(result_3)


def values_greater_than_second(ls):
    if len(ls) < 2:
        return False
    second_value = ls[1]
    new_list = [x for x in ls if x > second_value]
    print(len(new_list))
    return new_list


result_4 = values_greater_than_second([5, 2, 3, 8, 1, 9])
print(result_4)


def length_and_value(size, value):
    return [value] * size


print(length_and_value(10, 7))
print(length_and_value(50, 2))
