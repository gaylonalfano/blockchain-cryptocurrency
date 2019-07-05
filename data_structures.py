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
number_list = [1, 2, 3, -5]
print([el for el in number_list if el > 0])  # [1, 2, 3]
print([el > 0 for el in number_list])
print(all([el > 0 for el in number_list]))
