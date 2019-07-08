# simple_list = [1, 2, 3, 4]
# simple_list.extend([5, 6, 7])
# print(simple_list)
# del simple_list[0]
# print(simple_list)

# d = {"name": "Gaylon"}
# f = {"family": ["Ash", "Aaron", "Adrian", "Archie"]}
# e = f.copy()
# # print(f, e)

# # f["family"].extend(["Gaylon"])
# # print(f"F {'-'*10}\n {f}")
# # print(e)

# print(d.items())
# for k, v in d.items():
#     print(k, v)
# del d["name"]

# t = (1, 2, 3)
# print(t.index(1))
# # del(t[0])  Immutable!

# s = {"Max", "Manuel", "Gaylon", "Ashley", "Max"}
# del s["Max"]
# print(s)


# all and any functions
# number_list = [1, 2, 3, -5]
# print([el for el in number_list if el > 0])  # [1, 2, 3]
# print([el > 0 for el in number_list])
# print(all([el > 0 for el in number_list]))

# List unpacking
# simple_list = [1, 2, 3]
# a, b, c = simple_list
# print(a, b, c)

# super_long_list = [1, 3, 7, "hello", 2, 8, True, ["Archie", "Adrian", "Aaron"], 100]
# first, *middle, last = super_long_list
# print(first)
# print(middle)
# print(last)


# # List comprehension with sets
# new_set = {"Gaylon", "Ashley", 3}
# l = [el for el in new_set]
# print(l)
# # unpacking
# a, b, c = l
# print(a, b, c)


# # tuples and list comprehension
# new_tuple = (1, 2, 3)
# t = [i for i in new_tuple]
# print(t)
# for el in new_tuple:
#     print(el)

# tuple unpacking for n values
super_long_tuple = (1, 4, "Ash", "Adrian", "Archie", "Aaron")
first, second, *rest = super_long_tuple
print(first)
print(second)
print(rest)


# dictionaries and list comprehension
new_dict = {"name": "Gaylon", "age": 38}
dl = [k for k in new_dict]
print(dl)
dl2 = [v for (k, v) in new_dict.items()]
print(dl2)
dl3 = [(v, k) for (k, v) in new_dict.items()]
print(dl3)

a, b = new_dict
print(a, b)
