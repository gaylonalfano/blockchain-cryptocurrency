# My attempt:
# 1) Create a list of names and use a for loop to output the length of each name (len() ).
names = ['Robert', 'Archie', 'Rudolph', 'Cloud',
         'Raistlin', 'Miller', 'Fitz', 'Falco', 'Jon']
# for name in names:
#     print(len(name))


# 2) Add an if check inside the loop to only output names longer than 5 characters.
# for name in names:
#     if len(name) > 5:
#         print(name)


# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
#    If it does have an "n" or "N", then print the len(name)
for name in names:
    if len(name) > 5 and ("n" or "N") in name:
        print(f"{name} -- {len(name)}")
# 4) Use a while  loop to empty the list of names (via pop() )
while len(names) > 0:
    print(f"Popping: {names.pop()}!")
else:
    print(names)


# Instructor's
for name in names:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(name)
        print(len(name))

while len(names) >= 1:
    names.pop()

print(names)
