# Assignment for data structures module

# 1. Create a list of people
people = [
    {
        "name": "Gaylon",
        "age": 38,
        "hobbies": ["golf", "chinese", "chess", "swimming", "programming"],
    },
    {"name": "Ashley", "age": 38, "hobbies": ["art", "yoga", "reading", "facebook"]},
    {"name": "Adrian", "age": 8, "hobbies": ["nintendo", "reading", "lego"]},
]

# 2. Use list comprehension to retrieve names only
names = [person["name"] for person in people]
print(names)

# 3. Use list comprehension to check whether all are over age 20
over_20 = all([person["age"] > 20 for person in people])
print(over_20)

# 4. Make a deep copy of people dict and change 'name' value
copied_people = [person.copy() for person in people]
print(copied_people)
copied_people[0]["name"] = "Aaron"
print(copied_people)
print(people)


# 5. Unpack each person and store into different vars and output the vars
p1, p2, p3 = people
print(p1)
print(p2)
print(p3)
