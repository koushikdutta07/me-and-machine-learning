# ---------------- Dictionary Methods ----------------

student = {"name": "Koushik", "age": 22, "course": "IT"}

# 1. clear() - Removes all items
d = student.copy()
d.clear()
print("clear():", d)

# 2. copy() - Creates a copy
d = student.copy()
print("copy():", d)

# 3. fromkeys() - Creates a dictionary from given keys
keys = ["name", "age", "course"]
newDict = dict.fromkeys(keys, "N/A")
print("fromkeys():", newDict)

# 4. get() - Returns value of a key
print("get():", student.get("name"))
print("get() with default:", student.get("marks", 0))

# 5. items() - Returns key-value pairs
print("items():", student.items())
for key, value in student.items():
    print(key, "->", value)

# 6. keys() - Returns all keys
print("keys():", student.keys())
for key in student.keys():
    print(key)

# 7. pop() - Removes specified key
d = student.copy()
print("pop():", d.pop("age"))
print(d)

# 8. popitem() - Removes last inserted key-value pair
d = student.copy()
print("popitem():", d.popitem())
print(d)

# 9. setdefault() - Returns value if key exists, else inserts key
d = student.copy()
print("setdefault(existing):", d.setdefault("name", "Unknown"))
print("setdefault(new):", d.setdefault("city", "Kolkata"))
print(d)

# 10. update() - Updates dictionary
d = student.copy()
d.update({"age": 23, "city": "Kolkata"})
print("update():", d)

# 11. values() - Returns all values
print("values():", student.values())
for value in student.values():
    print(value)