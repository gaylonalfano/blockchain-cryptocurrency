# Section 5: Functions and Strings

name = "Gaylon"
age = 38
print("I am {} and I am {} years old".format(name, age))
# Change the order of placeholders
print("I am {1} and I am {0} years old".format(name, age))
# To resuse the argument you need to reference its index
print("I am {0} and I am {1} years old. {0} is a rare name.".format(name, age))
# Reference by name
print("I am {0} and I am {1} years old. {0} is a rare name.".format(name, age))
print(
    "I am {name} and I am {years} years old. {name} is a rare name.".format(
        name=name, years=age
    )
)

# Format the output
funds = 150.9723

print("Funds: {}".format(funds))
print("Funds: {:.1f}".format(funds))  # 151.0
print("Funds: {:.2f}".format(funds))  # 150.97
print("Funds: {:10.0f}".format(funds))  #           151
# Form the alignment
print("Funds: {:<10.2f}".format(funds))
print("Funds: {:>10.2f}".format(funds))
print("Funds: {:^10.2f}".format(funds))
# Fill in the empty space
print("Funds: {:-^10.2f}".format(funds))
print("Funds: {:=>10.2f}".format(funds))
print("Funds: {:%<10.2f}".format(funds))


# Using f-strings instead
print(f"I am {name} and I am {age:.2f} years old. I have {funds:-^10.2f} in funds.")


# map() function
simple_list = [1, 2, 3, 4]


def times_two(el):
    return el * 2


print(map(times_two, simple_list))
print(list(map(times_two, simple_list)))
print(list(map(str, simple_list)))


# lambda functions
list(map(lambda el: el * 2, simple_list))
