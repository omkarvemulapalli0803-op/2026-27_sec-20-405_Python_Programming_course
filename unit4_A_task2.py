d = {"name": "Omkar", "age": 18}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("name"))

d.update({"age": 19})
print(d)

d.pop("age")
print(d)