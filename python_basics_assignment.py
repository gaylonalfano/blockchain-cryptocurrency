# INSTRUCTOR'S
# 1.
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# 2.


# def print_user_data():
#     print(user_name + ' - ' + user_age)


# print_user_data()

# 3.


def print_concatenated_data(el1, el2):
    print(el1 + " - " + el2)


print_concatenated_data(user_name, user_age)


# 4.
def calculate_decades(age):
    """Calculates the integer part of the age received.

    Arguments:
        :param age: The age for which the decades should be calculated.

    Returns the decades lived.
    """
    decades_lived = int(age) // 10
    return decades_lived


decades = calculate_decades(int(user_age))
print(decades)


# MINE
# # name = input("Enter your name: ")
# # age = input('Enter your age: ')


# # def print_str():
# #     print("Hello, " + name + ", you are " + age + " years old.")


# # print_str()

# # def combine_into_two(arg1, arg2):
# #     """Returns any two arguments as one string"""
# #     print(str(arg1) + " and " + arg2 + " were entered.")


# # combine_into_two('Taco', 'Tuesday')


# def number_of_decades_lived():
#     """Calculates and returns the number of decades you've already lived"""
#     age = int(input("Enter your age: "))
#     decades_lived = age / 10
#     print(decades_lived)


# number_of_decades_lived()
