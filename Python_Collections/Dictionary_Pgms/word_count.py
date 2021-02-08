text = "hai how are you hai how are you"

# wordcount hai=2 how=2 are=2 you=2
words = text.split(" ")

dict = {}
for word in words:
    if (word not in dict):
        dict[word] = 1
    else:
        dict[word] += 1
print(dict)