s = input("Enter a sentence: ")
d = {}

for word in s.split():
    d[word] = d.get(word, 0) + 1

print(d)